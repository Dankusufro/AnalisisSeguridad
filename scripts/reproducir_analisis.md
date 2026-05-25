# Reproduccion del Analisis

Los scripts de analisis estan en `scripts/`:

- `analyze_results.py`: analiza SBOM, Grype y CodeQL.
- `analyze_cicd.py`: analiza workflows de GitHub Actions.
- `build_report_sections.py`: genera secciones Markdown y metricas finales.

## Reproducir resultados derivados

Desde la raiz de este proyecto (`AnalisisOpen`):

```bash
python3 scripts/analyze_results.py
python3 scripts/analyze_cicd.py
python3 scripts/build_report_sections.py
```

Salidas generadas:

- `results/generated/repositories_summary.csv`
- `results/generated/repositories_summary.md`
- `results/generated/grype_findings.csv`
- `results/generated/grype_findings.md`
- `results/generated/codeql_findings.csv`
- `results/generated/codeql_findings.md`
- `results/generated/cicd_risks.csv`
- `results/generated/cicd_risks.md`
- `results/generated/risk_prioritization.csv`
- `results/generated/risk_prioritization.md`
- `results/generated/readme_sections.md`
- `results/generated/proposal_metrics.json`

Entradas incluidas:

- SBOMs en `data/results/*-sbom.json`.
- Reportes Grype en `data/results/*-grype.json` y `data/results/*-grype-raw.json`.
- Reportes CodeQL en `data/results/*-codeql.json`.
- Tabla consolidada en `data/results/summary_table.md` y `data/results/summary_table.csv`.

Validacion rapida:

```bash
python3 -m compileall scripts
python3 scripts/analyze_results.py
python3 scripts/analyze_cicd.py
python3 scripts/build_report_sections.py
```
