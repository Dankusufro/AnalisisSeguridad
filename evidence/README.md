# Evidencia de la Propuesta

Esta carpeta documenta donde se encuentra la evidencia usada por `../README.md`.

La evidencia fuente esta incluida dentro de este proyecto para que funcione como repositorio independiente:

- `../data/results/summary_table.md`
- `../data/results/summary_table.csv`
- `../data/results/*-sbom.json`
- `../data/results/*-grype.json`
- `../data/results/*-grype-raw.json`
- `../data/results/*-codeql.json`
- `../data/repos.json`
- `../data/repos/*/.github/workflows/`
- `../scripts/`

La evidencia derivada creada para esta entrega esta en:

- `../results/generated/repositories_summary.csv`
- `../results/generated/repositories_summary.md`
- `../results/generated/grype_findings.csv`
- `../results/generated/grype_findings.md`
- `../results/generated/codeql_findings.csv`
- `../results/generated/codeql_findings.md`
- `../results/generated/cicd_risks.csv`
- `../results/generated/cicd_risks.md`
- `../results/generated/risk_prioritization.csv`
- `../results/generated/risk_prioritization.md`
- `../results/generated/readme_sections.md`
- `../results/generated/proposal_metrics.json`

## Evidencia resumida

| Tipo | Archivo o carpeta | Que respalda |
| --- | --- | --- |
| SBOM | `../data/results/*-sbom.json` | Componentes y ecosistemas detectados. |
| Grype | `../data/results/*-grype.json` | Vulnerabilidades conocidas en dependencias. |
| CodeQL | `../data/results/*-codeql.json` | Hallazgos de codigo fuente. |
| CI/CD | `../data/repos/*/.github/workflows/` | Riesgos en pipelines, acciones, secretos y permisos. |
| Scripts | `../scripts/` | Reproducibilidad del analisis. |
| Analisis generado | `../results/generated/` | Metricas y tablas usadas para priorizar. |

## Archivos CodeQL clave

- `../data/results/opencode-codeql.json`
- `../data/results/claude-code-action-codeql.json`
- `../data/results/maigret-codeql.json`
- `../data/results/jcode-codeql.json`
- `../data/results/ai-engineering-from-scratch-codeql.json`
- `../data/results/Anthropic-Cybersecurity-Skills-codeql.json`
- `../data/results/Understand-Anything-codeql.json`

## Workflows CI/CD clave

- `../data/repos/dexter/.github/workflows/rebase-on-label.yml`
- `../data/repos/opencode/.github/workflows/`
- `../data/repos/claude-code-action/.github/workflows/`
- `../data/repos/n8n-mcp/.github/workflows/`
- `../data/repos/maigret/.github/workflows/`
