# Guion de Presentacion Oral

Duracion maxima: 10 minutos.

## 1. Contexto

El analisis se realizo sobre los resultados disponibles en `data/results/` y sobre los workflows disponibles en `data/repos/`. Para esta entrega se crearon scripts en `scripts/` que consolidan SBOM, Grype, CodeQL y CI/CD en tablas dentro de `results/generated/`.

## 2. Mensaje principal

La gestion de vulnerabilidades no debe basarse solo en la cantidad de hallazgos. En este caso hay muchos hallazgos Grype, pero todos son de severidad baja. Los riesgos que deben atenderse primero estan en codigo fuente y CI/CD.

## 3. Metricas clave

| Metrica | Valor |
| --- | ---: |
| Repositorios con evidencia | 22 |
| Hallazgos Grype | 570 |
| Hallazgos CodeQL | 878 |
| Riesgos CI/CD | 570 |
| Grype criticas/altas/medias/bajas | 0/0/0/570 |
| CodeQL P0/P1/P2/P3 | 5/188/52/633 |
| CI/CD P0/P1/P2 | 11/255/304 |

## 4. Hallazgos principales

- `opencode`: P0 por `js/command-line-injection`, `js/indirect-command-line-injection` y `js/shell-command-injection-from-environment`.
- `Understand-Anything`: P0 por `js/shell-command-injection-from-environment`.
- `Anthropic-Cybersecurity-Skills`: P1 por logging y almacenamiento de datos sensibles y hashing debil.
- `claude-code-action`: P1 por XSS DOM, archivo-HTTP y filesystem con datos no confiables.
- `maigret`: P1 por log injection y hashing debil.
- `jcode`: P1 por logging de datos sensibles.
- `ruflo`, `n8n-mcp`, `presenton` y `TradingAgents`: P2 por alto volumen de vulnerabilidades Grype bajas.

## 5. Vectores de ataque

- Dependencias y codigo fuente: 570 hallazgos Grype bajos y hallazgos CodeQL P0/P1.
- Pipelines CI/CD: 570 riesgos, incluyendo `pull_request_target`, `id-token: write`, secretos, permisos write y acciones no fijadas por SHA.
- Humanos: necesidad de triage, revision de workflows, manejo correcto de secretos y aceptacion documentada de riesgos.

## 6. Ciclo Conozco -> Verifico -> Evidencio -> Decido y Actuo

Ejemplo P0: command injection en `opencode`.

| Paso | Aplicacion |
| --- | --- |
| Conozco | CodeQL reporta inyeccion de comandos. |
| Verifico | Se revisan regla, archivo, linea y flujo de datos en `codeql_findings.md`. |
| Evidencio | La evidencia queda en `results/generated/codeql_findings.csv` y `.md`. |
| Decido y Actuo | Se clasifica P0, se corrige la construccion de comandos y se bloquea release si es explotable. |

## 7. Priorizacion

| Prioridad | Ejemplos | Accion |
| --- | --- | --- |
| P0 | Command injection, `pull_request_target`, `id-token: write` critico | Mitigar inmediatamente. |
| P1 | Secretos en logs, XSS, permisos write, secretos en workflows | Corregir en corto plazo. |
| P2 | Vulnerabilidades Grype low, acciones no fijadas por SHA | Planificar actualizacion y hardening. |
| P3 | Sin hallazgos criticos o deuda tecnica menor | Monitorear. |

## 8. Acciones propuestas

- Corregir primero P0 en `opencode`, `Understand-Anything` y workflows criticos.
- Eliminar o aislar `pull_request_target` cuando procese PRs externos.
- Reducir permisos de workflows al minimo necesario.
- Separar workflows con secretos de workflows que ejecutan codigo no confiable.
- Fijar GitHub Actions por SHA completo.
- Eliminar secretos de logs y aplicar redaccion automatica.
- Actualizar dependencias en `ruflo`, `n8n-mcp`, `presenton` y `TradingAgents`.
- Mantener triage con responsables, plazos y evidencia.

## 9. Cierre

La propuesta reduce el riesgo porque convierte resultados de herramientas en decisiones. Primero se corrigen los riesgos explotables y de CI/CD, luego se atienden exposiciones de datos y finalmente se planifican actualizaciones de dependencias de severidad baja.

## Distribucion sugerida de tiempo

| Minuto | Contenido |
| --- | --- |
| 0:00 - 1:00 | Contexto y herramientas usadas. |
| 1:00 - 2:00 | Metricas clave. |
| 2:00 - 4:00 | Hallazgos principales P0/P1. |
| 4:00 - 5:30 | Vectores de ataque. |
| 5:30 - 7:00 | Ciclo Conozco -> Verifico -> Evidencio -> Decido y Actuo. |
| 7:00 - 8:30 | Priorizacion. |
| 8:30 - 9:30 | Acciones propuestas. |
| 9:30 - 10:00 | Conclusion. |
