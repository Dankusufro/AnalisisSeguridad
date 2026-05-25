#!/usr/bin/env python3
"""Analyze GitHub Actions workflows for supply-chain CI/CD risks."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPOS_DIR = ROOT / "data" / "repos"
DEFAULT_OUTPUT_DIR = ROOT / "results" / "generated"
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
USES_RE = re.compile(r"uses:\s*['\"]?([^\s'\"#]+)")


def workflow_files(repos_dir: Path) -> list[Path]:
    files: list[Path] = []
    for repo in sorted(path for path in repos_dir.iterdir() if path.is_dir()):
        workflows = repo / ".github" / "workflows"
        if workflows.exists():
            files.extend(sorted(workflows.glob("*.yml")))
            files.extend(sorted(workflows.glob("*.yaml")))
    return files


def repo_name(path: Path, repos_dir: Path) -> str:
    return path.relative_to(repos_dir).parts[0]


def detect_risks(path: Path, repos_dir: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    repo = repo_name(path, repos_dir)
    rel = str(path.relative_to(repos_dir / repo))
    risks: list[dict[str, Any]] = []

    def add(risk_type: str, priority: str, evidence: str, recommendation: str) -> None:
        risks.append(
            {
                "repo": repo,
                "workflow": rel,
                "risk_type": risk_type,
                "priority": priority,
                "evidence": evidence,
                "recommendation": recommendation,
            }
        )

    if "pull_request_target" in text:
        add(
            "pull_request_target",
            "P0",
            "El workflow usa pull_request_target.",
            "Evitar pull_request_target para codigo de PR externo o aislarlo sin checkout de codigo no confiable.",
        )

    if re.search(r"secrets\.[A-Za-z0-9_]+", text):
        add(
            "secrets_in_workflow",
            "P1",
            "El workflow referencia secrets.*.",
            "Separar workflows con secretos de validaciones de PR y usar environments protegidos.",
        )

    if re.search(r"permissions:\s*write-all", text):
        add(
            "write_all_permissions",
            "P0",
            "El workflow declara permissions: write-all.",
            "Reemplazar por permisos minimos por job.",
        )

    for permission in ("contents", "pull-requests", "issues", "packages", "id-token", "actions"):
        if re.search(rf"{re.escape(permission)}:\s*write", text):
            add(
                "write_permission",
                "P1" if permission != "id-token" else "P0",
                f"El workflow declara {permission}: write.",
                "Justificar el permiso y limitarlo al job que lo necesita.",
            )

    for match in USES_RE.finditer(text):
        action = match.group(1).strip()
        if "@" not in action:
            add(
                "action_without_ref",
                "P2",
                f"Accion sin referencia explicita: {action}.",
                "Fijar la accion por SHA completo.",
            )
            continue
        _, ref = action.rsplit("@", 1)
        if not SHA_RE.fullmatch(ref):
            priority = "P1" if not action.startswith("actions/") else "P2"
            add(
                "unpinned_action",
                priority,
                f"Accion no fijada por SHA: {action}.",
                "Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente.",
            )
    return risks


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze CI/CD workflow risks.")
    parser.add_argument("--repos-dir", type=Path, default=DEFAULT_REPOS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    risks: list[dict[str, Any]] = []
    workflow_count = 0
    for path in workflow_files(args.repos_dir):
        workflow_count += 1
        risks.extend(detect_risks(path, args.repos_dir))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "cicd_risks.csv", risks, ["repo", "workflow", "risk_type", "priority", "evidence", "recommendation"])

    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    top = sorted(risks, key=lambda row: (priority_order.get(str(row["priority"]), 9), row["repo"], row["workflow"], row["risk_type"]))[:150]
    (args.output_dir / "cicd_risks.md").write_text(
        "# Riesgos CI/CD\n\n"
        + markdown_table(
            ["Repositorio", "Workflow", "Prioridad", "Riesgo", "Evidencia", "Recomendacion"],
            [[row["repo"], row["workflow"], row["priority"], row["risk_type"], row["evidence"], row["recommendation"]] for row in top],
        ),
        encoding="utf-8",
    )

    by_repo: dict[str, Counter[str]] = defaultdict(Counter)
    for row in risks:
        by_repo[row["repo"]][row["priority"]] += 1
    summary_rows = [
        {
            "repo": repo,
            "p0": counts["P0"],
            "p1": counts["P1"],
            "p2": counts["P2"],
            "total": sum(counts.values()),
        }
        for repo, counts in sorted(by_repo.items())
    ]
    write_csv(args.output_dir / "cicd_summary.csv", summary_rows, ["repo", "p0", "p1", "p2", "total"])
    (args.output_dir / "cicd_summary.md").write_text(
        "# Resumen CI/CD por Repositorio\n\n"
        + markdown_table(
            ["Repositorio", "P0", "P1", "P2", "Total"],
            [[row["repo"], row["p0"], row["p1"], row["p2"], row["total"]] for row in summary_rows],
        ),
        encoding="utf-8",
    )
    (args.output_dir / "cicd_summary.json").write_text(
        json.dumps({"workflows_analyzed": workflow_count, "risks_found": len(risks), "repositories": len(summary_rows)}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Analisis CI/CD generado en {args.output_dir}")
    print(f"Workflows analizados: {workflow_count}")
    print(f"Riesgos CI/CD: {len(risks)}")


if __name__ == "__main__":
    main()
