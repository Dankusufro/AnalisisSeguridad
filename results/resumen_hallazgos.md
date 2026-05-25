# Resumen de Hallazgos

## Dependencias

Fuente: `../data/results/summary_table.md`.

Resultado principal: los scripts de `../scripts/` identifican 570 hallazgos Grype, todos de severidad baja. Los repositorios con mayor acumulacion son `ruflo`, `n8n-mcp`, `presenton` y `TradingAgents`.

Evidencia generada:

- `generated/grype_findings.csv`
- `generated/grype_findings.md`
- `generated/repositories_summary.md`
- `generated/proposal_metrics.json`

## Codigo Fuente

| Repositorio | Hallazgo relevante | Evidencia |
| --- | --- | --- |
| `opencode` | Command injection, shell command injection, filesystem con datos no confiables | `../data/results/opencode-codeql.json` |
| `claude-code-action` | XSS DOM, archivo-HTTP, temporales inseguros | `../data/results/claude-code-action-codeql.json` |
| `maigret` | Log injection, hashing debil | `../data/results/maigret-codeql.json` |
| `jcode` | Logging de datos sensibles | `../data/results/jcode-codeql.json` |
| `ai-engineering-from-scratch` | HTTP response splitting, logging de datos sensibles, MD5 | `../data/results/ai-engineering-from-scratch-codeql.json` |
| `Anthropic-Cybersecurity-Skills` | Logging/almacenamiento de datos sensibles, hashing debil, protocolos inseguros | `../data/results/Anthropic-Cybersecurity-Skills-codeql.json` |
| `Understand-Anything` | Shell command injection desde entorno, ReDoS | `../data/results/Understand-Anything-codeql.json` |

## CI/CD

| Repositorio | Riesgo relevante |
| --- | --- |
| `dexter` | `pull_request_target`, acciones no fijadas por SHA, permisos write |
| `opencode` | Workflows numerosos con secretos, permisos write y acciones no fijadas |
| `claude-code-action` | Acciones de terceros, secretos y permisos write |
| `n8n-mcp` | Workflows Docker/release con secretos y acciones externas |
| `maigret` | Publicacion Docker/Python con secretos y acciones no fijadas |

## Metricas generadas

| Metrica | Valor |
| --- | --- |
| Repositorios con evidencia | 22 |
| Hallazgos Grype | 570 |
| Hallazgos CodeQL | 878 |
| Riesgos CI/CD | 570 |
| Grype criticas/altas/medias/bajas | 0/0/0/570 |
| CodeQL P0/P1/P2/P3 | 5/188/52/633 |
| CI/CD P0/P1/P2 | 11/255/304 |
