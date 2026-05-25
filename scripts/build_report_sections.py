#!/usr/bin/env python3
"""Build Markdown sections for the final vulnerability management proposal."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_DIR = ROOT / "results" / "generated"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build report-ready Markdown sections.")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    args = parser.parse_args()

    repos = read_csv(args.input_dir / "repositories_summary.csv")
    grype = read_csv(args.input_dir / "grype_findings.csv")
    codeql = read_csv(args.input_dir / "codeql_findings.csv")
    cicd = read_csv(args.input_dir / "cicd_risks.csv")
    prioritization = read_csv(args.input_dir / "risk_prioritization.csv")

    dependency_counts = Counter(row.get("severity", "unknown") for row in grype)
    codeql_priority_counts = Counter(row.get("priority", "P3") for row in codeql)
    cicd_priority_counts = Counter(row.get("priority", "P3") for row in cicd)

    content = ["# Secciones Generadas para el README\n"]
    content.append("## Resumen cuantitativo\n")
    content.append(
        table(
            ["Metrica", "Valor"],
            [
                ["Repositorios con evidencia", len(repos)],
                ["Hallazgos Grype", len(grype)],
                ["Hallazgos CodeQL", len(codeql)],
                ["Riesgos CI/CD", len(cicd)],
                ["Grype criticas/altas/medias/bajas", f"{dependency_counts['critical']}/{dependency_counts['high']}/{dependency_counts['medium']}/{dependency_counts['low']}"],
                ["CodeQL P0/P1/P2/P3", f"{codeql_priority_counts['P0']}/{codeql_priority_counts['P1']}/{codeql_priority_counts['P2']}/{codeql_priority_counts['P3']}"],
                ["CI/CD P0/P1/P2", f"{cicd_priority_counts['P0']}/{cicd_priority_counts['P1']}/{cicd_priority_counts['P2']}"],
            ],
        )
    )

    content.append("## Repositorios priorizados\n")
    content.append(
        table(
            ["Repositorio", "Prioridad", "Evidencia", "Accion"],
            [[row["repo"], row["priority"], row["main_evidence"], row["recommended_action"]] for row in prioritization[:20]],
        )
    )

    content.append("## Evidencia por vector\n")
    content.append(
        table(
            ["Vector", "Datos generados", "Archivo"],
            [
                ["Dependencias", f"{len(grype)} hallazgos Grype", "results/generated/grype_findings.csv"],
                ["Codigo fuente", f"{len(codeql)} hallazgos CodeQL", "results/generated/codeql_findings.csv"],
                ["CI/CD", f"{len(cicd)} riesgos de workflows", "results/generated/cicd_risks.csv"],
                ["Priorizacion", f"{len(prioritization)} repositorios priorizados", "results/generated/risk_prioritization.csv"],
            ],
        )
    )

    summary = {
        "repositories": len(repos),
        "grype_findings": len(grype),
        "codeql_findings": len(codeql),
        "cicd_risks": len(cicd),
        "dependency_counts": dict(dependency_counts),
        "codeql_priority_counts": dict(codeql_priority_counts),
        "cicd_priority_counts": dict(cicd_priority_counts),
    }
    args.input_dir.mkdir(parents=True, exist_ok=True)
    (args.input_dir / "readme_sections.md").write_text("\n".join(content), encoding="utf-8")
    (args.input_dir / "proposal_metrics.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Secciones generadas en {args.input_dir / 'readme_sections.md'}")


if __name__ == "__main__":
    main()
