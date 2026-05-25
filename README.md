# Propuesta de Gestion de Vulnerabilidades

## 1. Contexto del analisis

Esta entrega corresponde a la actividad de seguridad de cadena de suministro de software. El objetivo es responder la pregunta central:

**Como deberia gestionar el equipo las vulnerabilidades encontradas, considerando su origen, su evidencia y el nivel de riesgo que representan?**

Para responderla se analizaron los resultados disponibles en `data/results/` y se crearon scripts propios dentro de `scripts/` para extraer valor de los JSON de SBOM, Grype, CodeQL y de los workflows de CI/CD.

La evidencia generada para esta entrega esta en `results/generated/`.

| Archivo generado | Proposito |
| --- | --- |
| `results/generated/repositories_summary.md` | Resumen por repositorio: componentes, ecosistemas, hallazgos Grype, CodeQL y prioridad. |
| `results/generated/grype_findings.md` | Vulnerabilidades de dependencias detectadas por Grype. |
| `results/generated/codeql_findings.md` | Hallazgos de codigo fuente detectados por CodeQL. |
| `results/generated/cicd_summary.md` | Resumen de riesgos CI/CD por repositorio. |
| `results/generated/cicd_risks.md` | Detalle de riesgos CI/CD en workflows. |
| `results/generated/risk_prioritization.md` | Priorizacion final por repositorio. |
| `results/generated/readme_sections.md` | Secciones Markdown generadas automaticamente. |
| `results/generated/proposal_metrics.json` | Metricas globales de la propuesta. |

Los scripts creados para obtener estos resultados son:

| Script | Funcion |
| --- | --- |
| `scripts/analyze_results.py` | Procesa SBOM, Grype y CodeQL desde `data/results/`. |
| `scripts/analyze_cicd.py` | Analiza workflows en `data/repos/*/.github/workflows/`. |
| `scripts/build_report_sections.py` | Genera metricas y tablas Markdown para el informe. |

## 2. Vulnerabilidades encontradas

El analisis generado identifica 22 repositorios con evidencia. Los resultados principales son:

| Metrica | Valor |
| --- | ---: |
| Repositorios con evidencia | 22 |
| Hallazgos Grype | 570 |
| Hallazgos CodeQL | 878 |
| Riesgos CI/CD | 570 |
| Grype criticas/altas/medias/bajas | 0/0/0/570 |
| CodeQL P0/P1/P2/P3 | 5/188/52/633 |
| CI/CD P0/P1/P2 | 11/255/304 |

La conclusion inicial es que las dependencias tienen muchos hallazgos, pero todos son de severidad baja. En cambio, el codigo fuente y los pipelines CI/CD concentran los riesgos de mayor prioridad.

### Resumen por repositorio

| Repositorio | Componentes | Ecosistemas | Grype | CodeQL | CodeQL seguridad | Prioridad |
| --- | ---: | --- | ---: | ---: | ---: | --- |
| `Anthropic-Cybersecurity-Skills` | 3 | github-actions | 0 | 194 | 183 | P1 |
| `DeepSeek-TUI` | 862 | cargo, github-actions | 12 | 0 | 0 | P2 |
| `FinceptTerminal` | 81 | github-actions, pip | 0 | 0 | 0 | P3 |
| `TradingAgents` | 201 | pip | 56 | 51 | 0 | P2 |
| `Understand-Anything` | 1083 | github-actions, npm | 16 | 11 | 11 | P0 |
| `agency-agents` | 1 | github-actions | 0 | 0 | 0 | P3 |
| `ai-engineering-from-scratch` | 2 | github-actions | 0 | 232 | 4 | P1 |
| `andrej-karpathy-skills` | 0 | No detectado | 0 | 0 | 0 | P3 |
| `chrome-devtools-mcp` | 11 | github-actions, npm | 0 | 0 | 0 | P3 |
| `claude-code-action` | 37 | github-actions, npm | 5 | 16 | 14 | P1 |
| `claude-plugins-official` | 14 | github-actions | 1 | 19 | 0 | P2 |
| `codegraph` | 15 | github-actions, npm | 2 | 0 | 0 | P2 |
| `dexter` | 243 | github-actions, npm | 11 | 0 | 0 | P2 |
| `genai-code-review` | 5 | github-actions, pip | 3 | 4 | 0 | P2 |
| `jcode` | 832 | cargo, github-actions | 8 | 57 | 4 | P1 |
| `maigret` | 150 | github-actions, pip | 3 | 76 | 9 | P1 |
| `n8n-mcp` | 1590 | github-actions, npm | 124 | 0 | 0 | P2 |
| `opencode` | 775 | cargo, github-actions | 15 | 218 | 17 | P0 |
| `presenton` | 1083 | github-actions, npm, pip | 65 | 0 | 0 | P2 |
| `qBittorrent` | 30 | github-actions | 0 | 0 | 0 | P3 |
| `ruflo` | 3773 | cargo, github-actions, npm, pip | 231 | 0 | 0 | P2 |
| `skills` | 370 | npm | 18 | 0 | 0 | P2 |

### Hallazgos de dependencias

Grype encontro 570 vulnerabilidades de dependencias, todas de severidad baja. Esto significa que no hay vulnerabilidades criticas, altas ni medias detectadas en los reportes procesados, pero si existe riesgo acumulado por volumen de dependencias y paquetes repetidos.

Repositorios con mayor cantidad de hallazgos Grype:

| Repositorio | Hallazgos Grype | Interpretacion |
| --- | ---: | --- |
| `ruflo` | 231 | Mayor acumulacion de riesgo bajo en dependencias cargo, npm y pip. |
| `n8n-mcp` | 124 | Alto volumen de dependencias npm. |
| `presenton` | 65 | Riesgo bajo acumulado en dependencias npm/pip. |
| `TradingAgents` | 56 | Riesgo bajo acumulado en dependencias pip. |
| `skills` | 18 | Riesgo bajo en npm. |
| `Understand-Anything` | 16 | Dependencias bajas, pero con CodeQL P0. |
| `opencode` | 15 | Dependencias bajas, pero con CodeQL P0. |

Ejemplos de paquetes reportados por Grype incluyen `aiohttp`, `langchain-core`, `langchain-openai`, `undici`, `vite`, `picomatch`, `actions/download-artifact`, `protobufjs`, `urllib3`, `rustls-webpki`, `bytes` y `quinn-proto`.

### Hallazgos de codigo fuente

CodeQL detecto 878 hallazgos. De ellos, 5 son P0 y 188 son P1. Los hallazgos P0 estan asociados a inyeccion de comandos.

| Repositorio | Prioridad | Hallazgo principal | Evidencia |
| --- | --- | --- | --- |
| `opencode` | P0 | `js/command-line-injection`, `js/indirect-command-line-injection`, `js/shell-command-injection-from-environment` | `results/generated/codeql_findings.md` |
| `Understand-Anything` | P0 | `js/shell-command-injection-from-environment` | `results/generated/codeql_findings.md` |
| `Anthropic-Cybersecurity-Skills` | P1 | `py/clear-text-logging-sensitive-data`, `py/clear-text-storage-sensitive-data`, `py/weak-sensitive-data-hashing` | `results/generated/codeql_findings.md` |
| `ai-engineering-from-scratch` | P1 | `py/clear-text-logging-sensitive-data`, `py/http-response-splitting`, `py/weak-sensitive-data-hashing` | `results/generated/codeql_findings.md` |
| `claude-code-action` | P1 | `js/file-access-to-http`, `js/http-to-file-access`, `js/xss-through-dom` | `results/generated/codeql_findings.md` |
| `jcode` | P1 | `py/clear-text-logging-sensitive-data` | `results/generated/codeql_findings.md` |
| `maigret` | P1 | `py/log-injection`, `py/weak-sensitive-data-hashing` | `results/generated/codeql_findings.md` |

### Hallazgos de CI/CD

El analisis de workflows detecto 570 riesgos CI/CD: 11 P0, 255 P1 y 304 P2.

| Repositorio | P0 | P1 | P2 | Total |
| --- | ---: | ---: | ---: | ---: |
| `opencode` | 6 | 62 | 90 | 158 |
| `ruflo` | 1 | 7 | 91 | 99 |
| `n8n-mcp` | 0 | 54 | 29 | 83 |
| `jcode` | 0 | 40 | 17 | 57 |
| `claude-code-action` | 2 | 25 | 29 | 56 |
| `DeepSeek-TUI` | 0 | 25 | 13 | 38 |
| `qBittorrent` | 0 | 20 | 17 | 37 |
| `maigret` | 1 | 16 | 10 | 27 |
| `dexter` | 1 | 4 | 6 | 11 |
| `genai-code-review` | 0 | 2 | 1 | 3 |
| `agency-agents` | 0 | 0 | 1 | 1 |

Los riesgos principales son:

- Uso de `pull_request_target` en `dexter` y `opencode`.
- Uso de `id-token: write` en workflows de publicacion o automatizacion.
- Workflows que referencian `secrets.*`.
- Permisos `contents: write`, `pull-requests: write`, `issues: write` y `packages: write`.
- Acciones no fijadas por SHA, usando referencias como `@main`, `@stable`, `@v1`, `@v2`, `@v3` o `@v4`.

## 3. Clasificacion segun vector de ataque

| Vector | Evidencia | Hallazgos principales | Riesgo |
| --- | --- | --- | --- |
| Dependencias y codigo fuente | `grype_findings.md`, `codeql_findings.md` | 570 vulnerabilidades Grype bajas, 5 CodeQL P0 y 188 CodeQL P1 | Alto cuando hay inyeccion de comandos; medio/bajo para dependencias low. |
| Pipelines CI/CD | `cicd_summary.md`, `cicd_risks.md` | 570 riesgos CI/CD, incluyendo `pull_request_target`, `id-token: write`, secretos y acciones no fijadas | Alto cuando combina PRs externos, permisos write y secretos. |
| Humanos | Proceso de revision, triage y aceptacion de riesgo | Falta de revision de workflows, dependencia excesiva en tags, secretos en automatizaciones, acumulacion de alertas | Medio, pero puede elevarse si el equipo ignora P0/P1. |

## 4. Analisis usando el ciclo Conozco -> Verifico -> Evidencio -> Decido y Actuo

### 4.1 Inyeccion de comandos en `opencode` y `Understand-Anything`

**Conozco:** CodeQL detecta reglas P0 en `opencode` y `Understand-Anything`. En `opencode` aparecen `js/command-line-injection`, `js/indirect-command-line-injection` y `js/shell-command-injection-from-environment`. En `Understand-Anything` aparece `js/shell-command-injection-from-environment`.

**Verifico:** se revisa `results/generated/codeql_findings.md`, que indica archivos, lineas y mensajes. En `opencode`, el archivo afectado es `packages/opencode/src/util/process.ts`, linea 62. En `Understand-Anything`, el hallazgo aparece en `understand-anything-plugin/src/__tests__/worktree-redirect.test.mjs`, linea 34.

**Evidencio:** la evidencia esta en `results/generated/codeql_findings.csv` y `results/generated/codeql_findings.md`.

**Decido y Actuo:** clasificar como P0. El equipo debe revisar si el flujo es explotable en produccion o solo en pruebas. Si es explotable, debe bloquear release, eliminar concatenacion de comandos, usar APIs con argumentos separados, validar allowlists y agregar pruebas con entradas maliciosas.

### 4.2 Exposicion de datos sensibles

**Conozco:** CodeQL reporta exposicion de datos sensibles en `Anthropic-Cybersecurity-Skills`, `jcode` y `ai-engineering-from-scratch`. Los hallazgos incluyen logging en texto claro, almacenamiento en texto claro y hashing debil.

**Verifico:** se revisan reglas como `py/clear-text-logging-sensitive-data`, `py/clear-text-storage-sensitive-data` y `py/weak-sensitive-data-hashing`.

**Evidencio:** `results/generated/codeql_findings.md` lista archivos y lineas afectadas. `Anthropic-Cybersecurity-Skills` concentra 183 hallazgos CodeQL de seguridad.

**Decido y Actuo:** clasificar como P1. El equipo debe eliminar secretos de logs, aplicar redaccion automatica, reemplazar hashing debil, usar gestores de secretos y crear pruebas que fallen si passwords, tokens o API keys se imprimen o almacenan en claro.

### 4.3 XSS, archivo-HTTP y filesystem con datos no confiables

**Conozco:** `claude-code-action` tiene hallazgos `js/xss-through-dom`, `js/file-access-to-http` y `js/http-to-file-access`.

**Verifico:** se revisa si los archivos afectados se exponen a usuarios, si procesan datos de PRs o si interactuan con contenido remoto.

**Evidencio:** `results/generated/codeql_findings.md` y `results/generated/codeql_findings.csv` documentan regla, archivo, linea y mensaje.

**Decido y Actuo:** clasificar como P1. Se debe evitar reinterpretar texto como HTML, usar APIs seguras como `textContent`, sanitizar entradas, validar rutas y restringir escrituras a directorios permitidos.

### 4.4 Dependencias con vulnerabilidades bajas

**Conozco:** Grype detecta 570 vulnerabilidades, todas low. No hay criticas, altas ni medias.

**Verifico:** se revisa `results/generated/grype_findings.md`, donde se observan paquetes, versiones, identificadores GHSA y mensajes.

**Evidencio:** `results/generated/grype_findings.csv`, `results/generated/grype_findings.md` y `results/generated/repositories_summary.md`.

**Decido y Actuo:** clasificar como P2. No se requiere respuesta de emergencia, pero si plan de actualizacion. Deben atenderse primero los repositorios con mayor acumulacion: `ruflo`, `n8n-mcp`, `presenton` y `TradingAgents`.

### 4.5 Riesgos CI/CD

**Conozco:** los workflows presentan 570 riesgos CI/CD. Existen 11 P0 asociados principalmente a `pull_request_target` e `id-token: write`.

**Verifico:** se revisa `results/generated/cicd_risks.md`, que indica workflow, riesgo, evidencia y recomendacion.

**Evidencio:** `results/generated/cicd_summary.md`, `results/generated/cicd_risks.md` y `results/generated/cicd_risks.csv`.

**Decido y Actuo:** clasificar como P0 o P1 segun el caso. Se debe eliminar o aislar `pull_request_target`, reducir permisos, justificar `id-token: write`, separar workflows con secretos de workflows de PR y fijar acciones por SHA.

### 4.6 Factor humano

**Conozco:** el riesgo humano se observa en decisiones repetidas: mantener acciones no fijadas, usar permisos amplios, acumular vulnerabilidades bajas y no separar secretos de flujos de PR.

**Verifico:** la evidencia muestra que los riesgos no son aislados. Hay 570 riesgos CI/CD y 570 hallazgos Grype, por lo que el equipo necesita proceso, no solo correcciones puntuales.

**Evidencio:** `proposal_metrics.json`, `cicd_summary.md`, `repositories_summary.md` y `risk_prioritization.md`.

**Decido y Actuo:** crear una politica de triage, asignar responsables, definir plazos por prioridad, exigir revision de cambios en `.github/workflows/`, capacitar en manejo de secretos y registrar aceptaciones de riesgo.

## 5. Priorizacion de vulnerabilidades

La priorizacion no se basa solo en cantidad. Se consideran severidad, facilidad de explotacion, impacto, exposicion y evidencia disponible.

| Prioridad | Criterio | Hallazgos incluidos | Accion |
| --- | --- | --- | --- |
| P0 | Puede permitir ejecucion de comandos, abuso de permisos o compromiso de CI/CD | Command injection, shell injection, `pull_request_target`, `id-token: write` sensible | Mitigar inmediatamente y bloquear release si aplica. |
| P1 | Puede exponer datos o permitir manipulacion relevante | Secretos en logs, almacenamiento en claro, XSS, filesystem con datos no confiables, permisos write, secretos en workflows | Corregir en corto plazo. |
| P2 | Riesgo bajo o acumulativo | Vulnerabilidades Grype low, acciones no fijadas por SHA, paquetes con historial de vulnerabilidades | Planificar actualizacion y monitoreo. |
| P3 | Sin hallazgos criticos o deuda tecnica menor | Repositorios sin hallazgos relevantes o advertencias de baja explotabilidad | Registrar y monitorear. |

Priorizacion final generada:

| Repositorio | Prioridad | Evidencia principal | Dependencias | CodeQL seguridad | Accion recomendada |
| --- | --- | --- | ---: | ---: | --- |
| `Understand-Anything` | P0 | `js/shell-command-injection-from-environment` | 16 | 11 | Mitigar de inmediato: revisar flujo explotable, corregir construccion de comandos y bloquear release si aplica. |
| `opencode` | P0 | `js/command-line-injection`; `js/indirect-command-line-injection`; `js/shell-command-injection-from-environment` | 15 | 17 | Mitigar de inmediato: revisar flujo explotable, corregir construccion de comandos y bloquear release si aplica. |
| `Anthropic-Cybersecurity-Skills` | P1 | `py/clear-text-logging-sensitive-data`; `py/clear-text-storage-sensitive-data`; `py/weak-sensitive-data-hashing` | 0 | 183 | Corregir en corto plazo: proteger datos sensibles, validar entradas y agregar pruebas de seguridad. |
| `ai-engineering-from-scratch` | P1 | `py/clear-text-logging-sensitive-data`; `py/http-response-splitting`; `py/weak-sensitive-data-hashing` | 0 | 4 | Corregir en corto plazo. |
| `claude-code-action` | P1 | `js/file-access-to-http`; `js/http-to-file-access`; `js/xss-through-dom` | 5 | 14 | Corregir en corto plazo. |
| `jcode` | P1 | `py/clear-text-logging-sensitive-data` | 8 | 4 | Corregir en corto plazo. |
| `maigret` | P1 | `py/log-injection`; `py/weak-sensitive-data-hashing` | 3 | 9 | Corregir en corto plazo. |
| `ruflo` | P2 | Dependencias vulnerables low y alto volumen CI/CD | 231 | 0 | Planificar actualizacion y hardening. |
| `n8n-mcp` | P2 | Dependencias vulnerables low y alto riesgo CI/CD P1 | 124 | 0 | Planificar actualizacion y hardening. |
| `presenton` | P2 | Dependencias vulnerables low | 65 | 0 | Planificar actualizacion. |
| `TradingAgents` | P2 | Dependencias vulnerables low | 56 | 0 | Planificar actualizacion. |

## 6. Acciones propuestas

### Acciones inmediatas P0

- Revisar `opencode` y `Understand-Anything` para confirmar si los flujos de inyeccion de comandos son explotables fuera de pruebas.
- Reemplazar construccion dinamica de comandos por APIs que separen ejecutable y argumentos.
- Validar entradas con allowlists y rechazar rutas o nombres de archivo no confiables.
- Bloquear release si el flujo P0 es alcanzable por usuarios, PRs externos o datos del entorno.
- Eliminar o aislar workflows con `pull_request_target` cuando procesen codigo de PR externo.
- Justificar y limitar `id-token: write` solo a jobs de publicacion que realmente lo necesiten.

### Acciones P1

- Eliminar logging de passwords, tokens, secretos y datos privados.
- Aplicar redaccion automatica antes de registrar errores o respuestas.
- Reemplazar hashing debil para datos sensibles por algoritmos adecuados al caso.
- Corregir XSS usando APIs seguras y sanitizacion.
- Restringir escrituras de archivos a rutas permitidas.
- Separar workflows con secretos de workflows que ejecutan codigo no confiable.
- Reducir permisos `contents: write`, `pull-requests: write`, `issues: write` y `packages: write` al minimo necesario.

### Acciones P2

- Planificar actualizaciones de dependencias en `ruflo`, `n8n-mcp`, `presenton` y `TradingAgents`.
- Revisar paquetes repetidos con vulnerabilidades low: `aiohttp`, `langchain`, `undici`, `vite`, `picomatch`, `protobufjs`, `urllib3` y `actions/download-artifact`.
- Fijar GitHub Actions por SHA completo.
- Ejecutar los scripts de `scripts/` despues de cada actualizacion para comparar resultados.
- Definir umbral de bloqueo: si Grype reporta una vulnerabilidad critica, alta o media explotable, el release debe detenerse.

### Acciones humanas y de proceso

- Asignar responsables de triage de seguridad.
- Definir plazos: P0 en 24 a 48 horas, P1 en una semana, P2 en el siguiente ciclo y P3 como deuda tecnica.
- Registrar estado de cada hallazgo: abierto, verificado, falso positivo, aceptado, mitigado o cerrado.
- Exigir revision obligatoria para cambios en `.github/workflows/`.
- Documentar aceptaciones de riesgo con evidencia y fecha de revision.
- Capacitar al equipo en manejo de secretos, revision de dependencias y seguridad de GitHub Actions.

## 7. Evidencia utilizada

| Evidencia | Ubicacion | Uso |
| --- | --- | --- |
| Metricas globales | `results/generated/proposal_metrics.json` | Resume cantidades totales por herramienta y prioridad. |
| Resumen por repositorio | `results/generated/repositories_summary.md` | Relaciona repositorios, ecosistemas, hallazgos y prioridad. |
| Hallazgos Grype | `results/generated/grype_findings.md` y `.csv` | Sustenta vulnerabilidades de dependencias. |
| Hallazgos CodeQL | `results/generated/codeql_findings.md` y `.csv` | Sustenta vulnerabilidades de codigo fuente. |
| Riesgos CI/CD | `results/generated/cicd_risks.md` y `.csv` | Sustenta riesgos de pipelines. |
| Resumen CI/CD | `results/generated/cicd_summary.md` y `.csv` | Permite comparar repositorios por P0/P1/P2. |
| Priorizacion | `results/generated/risk_prioritization.md` y `.csv` | Sustenta decisiones de mitigacion. |
| Scripts de analisis | `scripts/analyze_results.py`, `scripts/analyze_cicd.py`, `scripts/build_report_sections.py` | Permiten reproducir los resultados. |
| Evidencia primaria | `data/results/` y `data/repos/` | Contiene JSON originales, SBOMs, Grype, CodeQL y workflows. |

## 8. Conclusiones

El equipo debe gestionar las vulnerabilidades con una estrategia basada en evidencia y riesgo. Los resultados muestran que no basta con contar hallazgos: aunque Grype reporta 570 vulnerabilidades, todas son bajas. Los riesgos mas urgentes estan en codigo fuente y CI/CD, especialmente inyeccion de comandos, `pull_request_target`, `id-token: write`, secretos en workflows y permisos amplios.

La primera decision es atender P0 en `opencode`, `Understand-Anything` y workflows criticos. La segunda decision es corregir P1 relacionados con exposicion de datos sensibles, XSS, escrituras inseguras y permisos CI/CD. La tercera decision es gestionar P2 mediante actualizaciones planificadas, fijacion de acciones por SHA y monitoreo continuo.

Esta propuesta reduce el riesgo porque transforma los resultados de herramientas en un proceso operativo: conocer los hallazgos, verificarlos, evidenciarlos, priorizarlos y actuar con responsables, plazos y criterios claros.
