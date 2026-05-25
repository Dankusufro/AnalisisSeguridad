#!/usr/bin/env python3
"""Analyze SBOM, Grype and CodeQL JSON files for the vulnerability proposal."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS_DIR = ROOT / "data" / "results"
DEFAULT_OUTPUT_DIR = ROOT / "results" / "generated"

SEVERITIES = ["critical", "high", "medium", "low", "negligible", "unknown"]
SECURITY_RULE_KEYWORDS = (
    "injection",
    "xss",
    "request-forgery",
    "sensitive",
    "hash",
    "debug",
    "protocol",
    "redos",
    "temporary-file",
    "file-access",
    "http-to-file",
    "csrf",
    "path",
    "command",
    "sql",
    "ssrf",
    "storage",
    "logging",
    "clear-text",
)
P0_RULE_KEYWORDS = ("command-line-injection", "shell-command-injection")
P1_RULE_KEYWORDS = (
    "xss",
    "sensitive",
    "clear-text",
    "request-forgery",
    "http-response-splitting",
    "file-access",
    "http-to-file",
    "weak-sensitive-data-hashing",
    "log-injection",
)


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def normalize_repo_name(path: Path) -> str:
    name = path.name
    for suffix in (
        "-grype-raw.json",
        "_grype_raw.json",
        "-codeql.json",
        "_codeql.json",
        "-grype.json",
        "_grype.json",
        "-sbom.json",
        "_sbom.json",
        "_temp.sarif",
        ".sarif",
        ".json",
    ):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem


def is_sbom(path: Path, data: dict[str, Any]) -> bool:
    lower = path.name.lower()
    return lower.endswith("-sbom.json") or any(key in data for key in ("artifacts", "components", "packages"))


def is_grype(path: Path, data: dict[str, Any]) -> bool:
    lower = path.name.lower()
    return lower.endswith("-grype.json") or lower.endswith("-grype-raw.json") or "matches" in data or "vulnerabilities" in data


def is_codeql(path: Path, data: dict[str, Any]) -> bool:
    return path.name.lower().endswith("-codeql.json") or "issues" in data


def sbom_items(data: dict[str, Any]) -> list[dict[str, Any]]:
    for key in ("artifacts", "components", "packages"):
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    return []


def detect_ecosystems(items: list[dict[str, Any]]) -> str:
    ecosystems: set[str] = set()
    for item in items:
        purl = str(item.get("purl") or "")
        item_type = str(item.get("type") or "").lower()
        language = str(item.get("language") or "").lower()
        if purl.startswith("pkg:npm/") or item_type in {"npm", "javascript", "node"} or language == "javascript":
            ecosystems.add("npm")
        elif purl.startswith("pkg:pypi/") or item_type in {"python", "pypi"} or language == "python":
            ecosystems.add("pip")
        elif purl.startswith("pkg:cargo/") or item_type in {"rust", "cargo"} or language == "rust":
            ecosystems.add("cargo")
        elif purl.startswith("pkg:golang/") or item_type in {"go", "go-module"}:
            ecosystems.add("go")
        elif purl.startswith("pkg:maven/") or item_type in {"maven", "java-archive"}:
            ecosystems.add("maven")
        elif purl.startswith("pkg:gem/"):
            ecosystems.add("ruby")
        elif purl.startswith("pkg:github/") or item_type == "github-action":
            ecosystems.add("github-actions")
    return ", ".join(sorted(ecosystems)) if ecosystems else "No detectado"


def read_grype_vulnerabilities(repo: str, path: Path, data: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    simplified = data.get("vulnerabilities")
    if isinstance(simplified, list):
        for vuln in simplified:
            if not isinstance(vuln, dict):
                continue
            severity = str(vuln.get("vuln_severity") or "unknown").lower()
            findings.append(
                {
                    "repo": repo,
                    "source_file": path.name,
                    "package_name": vuln.get("package_name", ""),
                    "current_version": vuln.get("current_version", ""),
                    "vulnerability_id": vuln.get("vuln_id", ""),
                    "severity": severity if severity in SEVERITIES else "unknown",
                    "fix_version": vuln.get("fix_version", ""),
                    "message": vuln.get("message", ""),
                    "cwe": vuln.get("cwe", ""),
                    "cvss_score": vuln.get("cvss_score", ""),
                }
            )
        return findings

    matches = data.get("matches")
    if isinstance(matches, list):
        for match in matches:
            if not isinstance(match, dict):
                continue
            vulnerability = match.get("vulnerability") or {}
            artifact = match.get("artifact") or {}
            severity = str(vulnerability.get("severity") or "unknown").lower()
            fix_versions = vulnerability.get("fix", {}).get("versions", []) if isinstance(vulnerability.get("fix"), dict) else []
            findings.append(
                {
                    "repo": repo,
                    "source_file": path.name,
                    "package_name": artifact.get("name", ""),
                    "current_version": artifact.get("version", ""),
                    "vulnerability_id": vulnerability.get("id", ""),
                    "severity": severity if severity in SEVERITIES else "unknown",
                    "fix_version": "; ".join(map(str, fix_versions)),
                    "message": vulnerability.get("description") or vulnerability.get("dataSource") or "",
                    "cwe": "; ".join(map(str, vulnerability.get("cwes", []))) if isinstance(vulnerability.get("cwes"), list) else "",
                    "cvss_score": best_cvss_score(vulnerability),
                }
            )
    return findings


def best_cvss_score(vulnerability: dict[str, Any]) -> str:
    scores: list[float] = []
    for cvss in vulnerability.get("cvss", []) if isinstance(vulnerability.get("cvss"), list) else []:
        if isinstance(cvss, dict):
            metrics = cvss.get("metrics") or {}
            score = metrics.get("baseScore")
            if isinstance(score, (int, float)):
                scores.append(float(score))
    return str(max(scores)) if scores else ""


def read_codeql_issues(repo: str, path: Path, data: dict[str, Any]) -> list[dict[str, Any]]:
    issues = data.get("issues")
    if not isinstance(issues, list):
        return []
    findings: list[dict[str, Any]] = []
    for issue in issues:
        if not isinstance(issue, dict):
            continue
        rule_id = str(issue.get("rule_id") or issue.get("ruleId") or "")
        region = issue.get("region") or {}
        if not isinstance(region, dict):
            region = {}
        security_relevant = any(keyword in rule_id.lower() for keyword in SECURITY_RULE_KEYWORDS)
        findings.append(
            {
                "repo": repo,
                "source_file": path.name,
                "rule_id": rule_id,
                "level": issue.get("level", "unknown"),
                "security_relevant": "yes" if security_relevant else "no",
                "priority": classify_codeql_priority(rule_id),
                "file": issue.get("file", ""),
                "line": region.get("startLine", ""),
                "message": str(issue.get("message", "")).replace("\n", " "),
            }
        )
    return findings


def classify_codeql_priority(rule_id: str) -> str:
    lower = rule_id.lower()
    if any(keyword in lower for keyword in P0_RULE_KEYWORDS):
        return "P0"
    if any(keyword in lower for keyword in P1_RULE_KEYWORDS):
        return "P1"
    if any(keyword in lower for keyword in SECURITY_RULE_KEYWORDS):
        return "P2"
    return "P3"


def classify_dependency_priority(severity_counts: Counter[str]) -> str:
    if severity_counts["critical"] or severity_counts["high"]:
        return "P1"
    if severity_counts["medium"] or severity_counts["low"]:
        return "P2"
    return "P3"


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        cleaned = [str(value).replace("\n", " ").replace("|", "\\|") for value in row]
        lines.append("| " + " | ".join(cleaned) + " |")
    return "\n".join(lines) + "\n"


def write_markdown(path: Path, title: str, headers: list[str], rows: list[list[Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n" + markdown_table(headers, rows), encoding="utf-8")


def collect(results_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    sbom_by_repo: dict[str, dict[str, Any]] = {}
    grype_findings: list[dict[str, Any]] = []
    codeql_findings: list[dict[str, Any]] = []
    files_by_repo: dict[str, set[str]] = defaultdict(set)

    for path in sorted(results_dir.glob("*.json")):
        data = load_json(path)
        if data is None:
            continue
        repo = normalize_repo_name(path)
        files_by_repo[repo].add(path.name)
        if is_sbom(path, data):
            items = sbom_items(data)
            sbom_by_repo[repo] = {
                "repo": repo,
                "sbom_file": path.name,
                "components": len(items),
                "ecosystems": detect_ecosystems(items),
            }
        if is_grype(path, data) and "raw" not in path.name.lower():
            grype_findings.extend(read_grype_vulnerabilities(repo, path, data))
        if is_codeql(path, data):
            codeql_findings.extend(read_codeql_issues(repo, path, data))

    repos = sorted(set(sbom_by_repo) | {row["repo"] for row in grype_findings} | {row["repo"] for row in codeql_findings})
    grype_by_repo: dict[str, Counter[str]] = defaultdict(Counter)
    for finding in grype_findings:
        grype_by_repo[finding["repo"]][finding["severity"]] += 1

    codeql_by_repo: dict[str, Counter[str]] = defaultdict(Counter)
    codeql_security_by_repo: dict[str, int] = defaultdict(int)
    p0_by_repo: dict[str, int] = defaultdict(int)
    p1_by_repo: dict[str, int] = defaultdict(int)
    for finding in codeql_findings:
        repo = finding["repo"]
        codeql_by_repo[repo][str(finding["level"])] += 1
        if finding["security_relevant"] == "yes":
            codeql_security_by_repo[repo] += 1
        if finding["priority"] == "P0":
            p0_by_repo[repo] += 1
        elif finding["priority"] == "P1":
            p1_by_repo[repo] += 1

    repository_rows: list[dict[str, Any]] = []
    for repo in repos:
        sbom = sbom_by_repo.get(repo, {})
        sev = grype_by_repo[repo]
        total_grype = sum(sev.values())
        total_codeql = sum(codeql_by_repo[repo].values())
        priority = "P0" if p0_by_repo[repo] else "P1" if p1_by_repo[repo] else classify_dependency_priority(sev)
        repository_rows.append(
            {
                "repo": repo,
                "sbom_file": sbom.get("sbom_file", "No detectado"),
                "components": sbom.get("components", 0),
                "ecosystems": sbom.get("ecosystems", "No detectado"),
                "grype_total": total_grype,
                "critical": sev["critical"],
                "high": sev["high"],
                "medium": sev["medium"],
                "low": sev["low"],
                "codeql_total": total_codeql,
                "codeql_security": codeql_security_by_repo[repo],
                "priority": priority,
                "evidence_files": "; ".join(sorted(files_by_repo[repo])),
            }
        )
    return repository_rows, grype_findings, codeql_findings, build_prioritization(repository_rows, grype_findings, codeql_findings)


def build_prioritization(
    repository_rows: list[dict[str, Any]], grype_findings: list[dict[str, Any]], codeql_findings: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    grype_by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    codeql_by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in grype_findings:
        grype_by_repo[row["repo"]].append(row)
    for row in codeql_findings:
        codeql_by_repo[row["repo"]].append(row)

    rows: list[dict[str, Any]] = []
    for repo_row in repository_rows:
        repo = repo_row["repo"]
        p0_rules = sorted({item["rule_id"] for item in codeql_by_repo[repo] if item["priority"] == "P0"})
        p1_rules = sorted({item["rule_id"] for item in codeql_by_repo[repo] if item["priority"] == "P1"})
        vuln_packages = sorted({item["package_name"] for item in grype_by_repo[repo] if item.get("package_name")})[:8]
        priority = repo_row["priority"]
        if priority == "P0":
            action = "Mitigar de inmediato: revisar flujo explotable, corregir construccion de comandos y bloquear release si aplica."
        elif priority == "P1":
            action = "Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad."
        elif priority == "P2":
            action = "Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening."
        else:
            action = "Registrar como deuda tecnica y resolver despues de riesgos altos."
        rows.append(
            {
                "repo": repo,
                "priority": priority,
                "main_evidence": "; ".join(p0_rules or p1_rules or vuln_packages or ["Sin hallazgos criticos"]),
                "dependency_findings": repo_row["grype_total"],
                "codeql_security_findings": repo_row["codeql_security"],
                "recommended_action": action,
            }
        )
    order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    return sorted(rows, key=lambda row: (order.get(str(row["priority"]), 9), str(row["repo"])))


def write_outputs(output_dir: Path, repository_rows: list[dict[str, Any]], grype_findings: list[dict[str, Any]], codeql_findings: list[dict[str, Any]], prioritization: list[dict[str, Any]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(
        output_dir / "repositories_summary.csv",
        repository_rows,
        ["repo", "sbom_file", "components", "ecosystems", "grype_total", "critical", "high", "medium", "low", "codeql_total", "codeql_security", "priority", "evidence_files"],
    )
    write_csv(
        output_dir / "grype_findings.csv",
        grype_findings,
        ["repo", "source_file", "package_name", "current_version", "vulnerability_id", "severity", "fix_version", "message", "cwe", "cvss_score"],
    )
    write_csv(
        output_dir / "codeql_findings.csv",
        codeql_findings,
        ["repo", "source_file", "rule_id", "level", "security_relevant", "priority", "file", "line", "message"],
    )
    write_csv(
        output_dir / "risk_prioritization.csv",
        prioritization,
        ["repo", "priority", "main_evidence", "dependency_findings", "codeql_security_findings", "recommended_action"],
    )

    write_markdown(
        output_dir / "repositories_summary.md",
        "Resumen por Repositorio",
        ["Repositorio", "Componentes", "Ecosistemas", "Grype", "CodeQL", "CodeQL seguridad", "Prioridad"],
        [[r["repo"], r["components"], r["ecosystems"], r["grype_total"], r["codeql_total"], r["codeql_security"], r["priority"]] for r in repository_rows],
    )
    top_grype = sorted(grype_findings, key=lambda r: (SEVERITIES.index(r["severity"]) if r["severity"] in SEVERITIES else 9, r["repo"], r["package_name"]))[:100]
    write_markdown(
        output_dir / "grype_findings.md",
        "Hallazgos Grype",
        ["Repositorio", "Paquete", "Version", "Vulnerabilidad", "Severidad", "Mensaje"],
        [[r["repo"], r["package_name"], r["current_version"], r["vulnerability_id"], r["severity"], r["message"][:120]] for r in top_grype],
    )
    top_codeql = sorted(codeql_findings, key=lambda r: ({"P0": 0, "P1": 1, "P2": 2, "P3": 3}.get(str(r["priority"]), 9), r["repo"], r["rule_id"]))[:100]
    write_markdown(
        output_dir / "codeql_findings.md",
        "Hallazgos CodeQL",
        ["Repositorio", "Prioridad", "Regla", "Archivo", "Linea", "Mensaje"],
        [[r["repo"], r["priority"], r["rule_id"], r["file"], r["line"], r["message"][:120]] for r in top_codeql],
    )
    write_markdown(
        output_dir / "risk_prioritization.md",
        "Priorizacion de Riesgo",
        ["Repositorio", "Prioridad", "Evidencia principal", "Dependencias", "CodeQL seguridad", "Accion recomendada"],
        [[r["repo"], r["priority"], r["main_evidence"], r["dependency_findings"], r["codeql_security_findings"], r["recommended_action"]] for r in prioritization],
    )
    summary = {
        "repositories": len(repository_rows),
        "grype_findings": len(grype_findings),
        "codeql_findings": len(codeql_findings),
        "codeql_security_findings": sum(1 for row in codeql_findings if row["security_relevant"] == "yes"),
        "priorities": dict(Counter(row["priority"] for row in prioritization)),
    }
    (output_dir / "analysis_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze SBOM, Grype and CodeQL results.")
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    repository_rows, grype_findings, codeql_findings, prioritization = collect(args.results_dir)
    write_outputs(args.output_dir, repository_rows, grype_findings, codeql_findings, prioritization)
    print(f"Analisis generado en {args.output_dir}")
    print(f"Repositorios: {len(repository_rows)}")
    print(f"Hallazgos Grype: {len(grype_findings)}")
    print(f"Hallazgos CodeQL: {len(codeql_findings)}")


if __name__ == "__main__":
    main()
