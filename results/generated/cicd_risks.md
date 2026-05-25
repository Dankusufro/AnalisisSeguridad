# Riesgos CI/CD

| Repositorio | Workflow | Prioridad | Riesgo | Evidencia | Recomendacion |
| --- | --- | --- | --- | --- | --- |
| claude-code-action | .github/workflows/claude-review.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/claude.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| dexter | .github/workflows/rebase-on-label.yml | P0 | pull_request_target | El workflow usa pull_request_target. | Evitar pull_request_target para codigo de PR externo o aislarlo sin checkout de codigo no confiable. |
| maigret | .github/workflows/python-publish.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| opencode | .github/workflows/docs-update.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| opencode | .github/workflows/opencode.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| opencode | .github/workflows/pr-management.yml | P0 | pull_request_target | El workflow usa pull_request_target. | Evitar pull_request_target para codigo de PR externo o aislarlo sin checkout de codigo no confiable. |
| opencode | .github/workflows/pr-standards.yml | P0 | pull_request_target | El workflow usa pull_request_target. | Evitar pull_request_target para codigo de PR externo o aislarlo sin checkout de codigo no confiable. |
| opencode | .github/workflows/publish.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| opencode | .github/workflows/review.yml | P0 | pull_request_target | El workflow usa pull_request_target. | Evitar pull_request_target para codigo de PR externo o aislarlo sin checkout de codigo no confiable. |
| ruflo | .github/workflows/pages.yml | P0 | write_permission | El workflow declara id-token: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| DeepSeek-TUI | .github/workflows/auto-tag.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| DeepSeek-TUI | .github/workflows/auto-tag.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: goto-bus-stop/setup-zig@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-qemu-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-buildx-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v5. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: softprops/action-gh-release@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| DeepSeek-TUI | .github/workflows/release.yml | P1 | write_permission | El workflow declara packages: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: oven-sh/setup-bun@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: oven-sh/setup-bun@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: oven-sh/setup-bun@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/claude-review.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/claude-review.yml | P1 | unpinned_action | Accion no fijada por SHA: anthropics/claude-code-action@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/claude-review.yml | P1 | write_permission | El workflow declara pull-requests: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/claude.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/claude.yml | P1 | unpinned_action | Accion no fijada por SHA: anthropics/claude-code-action@main. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/claude.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/claude.yml | P1 | write_permission | El workflow declara pull-requests: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/claude.yml | P1 | write_permission | El workflow declara issues: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/issue-triage.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/issue-triage.yml | P1 | unpinned_action | Accion no fijada por SHA: anthropics/claude-code-action@main. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| claude-code-action | .github/workflows/issue-triage.yml | P1 | write_permission | El workflow declara issues: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/non-write-users-check.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/non-write-users-check.yml | P1 | write_permission | El workflow declara pull-requests: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/release.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/release.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/sync-base-action.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/sync-base-action.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| claude-code-action | .github/workflows/test-base-action.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/test-custom-executables.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/test-mcp-servers.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/test-settings.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| claude-code-action | .github/workflows/test-structured-output.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| dexter | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: oven-sh/setup-bun@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| dexter | .github/workflows/rebase-on-label.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| dexter | .github/workflows/rebase-on-label.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| dexter | .github/workflows/rebase-on-label.yml | P1 | write_permission | El workflow declara pull-requests: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| genai-code-review | .github/workflows/genai_code_review.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| genai-code-review | .github/workflows/genai_code_review.yml | P1 | unpinned_action | Accion no fijada por SHA: cirolini/genai-code-review@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: ilammy/msvc-dev-cmd@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/ci.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: webfactory/ssh-agent@v0.9.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: ilammy/msvc-dev-cmd@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: ilammy/msvc-dev-cmd@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | unpinned_action | Accion no fijada por SHA: softprops/action-gh-release@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/release.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: ilammy/msvc-dev-cmd@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: ilammy/msvc-dev-cmd@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: dtolnay/rust-toolchain@stable. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: mozilla-actions/sccache-action@v0.0.7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| jcode | .github/workflows/windows-smoke.yml | P1 | unpinned_action | Accion no fijada por SHA: Swatinem/rust-cache@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-qemu-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-buildx-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v5. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v5. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/build-docker-image.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/codeql-analysis.yml | P1 | unpinned_action | Accion no fijada por SHA: github/codeql-action/init@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/codeql-analysis.yml | P1 | unpinned_action | Accion no fijada por SHA: github/codeql-action/autobuild@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/codeql-analysis.yml | P1 | unpinned_action | Accion no fijada por SHA: github/codeql-action/analyze@v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/pyinstaller.yml | P1 | unpinned_action | Accion no fijada por SHA: JackMcKew/pyinstaller-action-windows@main. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/pyinstaller.yml | P1 | unpinned_action | Accion no fijada por SHA: ncipollo/release-action@v1.14.0. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/python-publish.yml | P1 | unpinned_action | Accion no fijada por SHA: pypa/gh-action-pypi-publish@release/v1. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| maigret | .github/workflows/update-site-data.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| maigret | .github/workflows/update-site-data.yml | P1 | unpinned_action | Accion no fijada por SHA: peter-evans/create-pull-request@v7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-buildx-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-fast.yml | P1 | write_permission | El workflow declara packages: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-qemu-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-buildx-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | unpinned_action | Accion no fijada por SHA: softprops/action-gh-release@v2. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | write_permission | El workflow declara contents: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| n8n-mcp | .github/workflows/docker-build-n8n.yml | P1 | write_permission | El workflow declara packages: write. | Justificar el permiso y limitarlo al job que lo necesita. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | secrets_in_workflow | El workflow referencia secrets.*. | Separar workflows con secretos de validaciones de PR y usar environments protegidos. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-qemu-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-buildx-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/metadata-action@v6. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/build-push-action@v7. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/login-action@v3. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
| n8n-mcp | .github/workflows/docker-build.yml | P1 | unpinned_action | Accion no fijada por SHA: docker/setup-qemu-action@v4. | Reemplazar tag o rama por SHA completo y revisar actualizaciones periodicamente. |
