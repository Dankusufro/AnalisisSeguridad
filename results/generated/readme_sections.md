# Secciones Generadas para el README

## Resumen cuantitativo

| Metrica | Valor |
| --- | --- |
| Repositorios con evidencia | 22 |
| Hallazgos Grype | 570 |
| Hallazgos CodeQL | 878 |
| Riesgos CI/CD | 570 |
| Grype criticas/altas/medias/bajas | 0/0/0/570 |
| CodeQL P0/P1/P2/P3 | 5/188/52/633 |
| CI/CD P0/P1/P2 | 11/255/304 |

## Repositorios priorizados

| Repositorio | Prioridad | Evidencia | Accion |
| --- | --- | --- | --- |
| Understand-Anything | P0 | js/shell-command-injection-from-environment | Mitigar de inmediato: revisar flujo explotable, corregir construccion de comandos y bloquear release si aplica. |
| opencode | P0 | js/command-line-injection; js/indirect-command-line-injection; js/shell-command-injection-from-environment | Mitigar de inmediato: revisar flujo explotable, corregir construccion de comandos y bloquear release si aplica. |
| Anthropic-Cybersecurity-Skills | P1 | py/clear-text-logging-sensitive-data; py/clear-text-storage-sensitive-data; py/weak-sensitive-data-hashing | Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| ai-engineering-from-scratch | P1 | py/clear-text-logging-sensitive-data; py/http-response-splitting; py/weak-sensitive-data-hashing | Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| claude-code-action | P1 | js/file-access-to-http; js/http-to-file-access; js/xss-through-dom | Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| jcode | P1 | py/clear-text-logging-sensitive-data | Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| maigret | P1 | py/log-injection; py/weak-sensitive-data-hashing | Corregir en el corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| DeepSeek-TUI | P2 | actions/download-artifact; aws-lc-sys; bytes; lru; quinn-proto; rand; rustls-webpki; time | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| TradingAgents | P2 | aiohttp; chainlit; curl-cffi; filelock; langchain-community; langchain-core; langchain-openai; langchain-text-splitters | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| claude-plugins-official | P2 | actions/download-artifact | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| codegraph | P2 | picomatch | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| dexter | P2 | file-type; langsmith; music-metadata; protobufjs; uuid | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| genai-code-review | P2 | requests | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| n8n-mcp | P2 | @azure/identity; @grpc/grpc-js; @hono/node-server; @langchain/community; @langchain/core; @supabase/auth-js; @tootallnate/once; @xmldom/xmldom | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| presenton | P2 | @isaacs/brace-expansion; authlib; axios; brace-expansion; dompurify; follow-redirects; glob; idna | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| ruflo | P2 | @anthropic-ai/claude-code; @hono/node-server; @isaacs/brace-expansion; @modelcontextprotocol/sdk; @sveltejs/kit; @tootallnate/once; actions/download-artifact; ajv | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| skills | P2 | @hono/node-server; basic-ftp; hono; langsmith; path-to-regexp; protobufjs; uuid | Planificar actualizacion y monitoreo: revisar paquetes afectados y aplicar hardening. |
| FinceptTerminal | P3 | Sin hallazgos criticos | Registrar como deuda tecnica y resolver despues de riesgos altos. |
| agency-agents | P3 | Sin hallazgos criticos | Registrar como deuda tecnica y resolver despues de riesgos altos. |
| andrej-karpathy-skills | P3 | Sin hallazgos criticos | Registrar como deuda tecnica y resolver despues de riesgos altos. |

## Evidencia por vector

| Vector | Datos generados | Archivo |
| --- | --- | --- |
| Dependencias | 570 hallazgos Grype | results/generated/grype_findings.csv |
| Codigo fuente | 878 hallazgos CodeQL | results/generated/codeql_findings.csv |
| CI/CD | 570 riesgos de workflows | results/generated/cicd_risks.csv |
| Priorizacion | 22 repositorios priorizados | results/generated/risk_prioritization.csv |
