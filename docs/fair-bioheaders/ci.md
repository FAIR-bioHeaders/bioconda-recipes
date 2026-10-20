# FAIR BioHeaders fork checks

This fork maintains FAIR BioHeaders packaging contributions within upstream
Bioconda conventions. It does not publish a separate channel or impose new rules
on unrelated packages.

## Why previous documentation PRs had no checks

At the October 20, 2026 inspection, repository Actions permissions reported
`enabled: true`, but the workflow API listed only the dynamic Copilot reviewer,
not any file-based workflows. No recent file-based runs were available. The
inherited `.github/workflows/PR.yml` has no documentation path filter and accepts
opened/synchronize/reopened PR events, so documentation filtering does not explain
the missing jobs. File presence and enabled repository permissions alone did not
establish active workflow registration/execution in this fork.

This evidence identifies a workflow activation/registration gap; it does not
establish the underlying fork-administration setting or permission history.
Do not enable all inherited publishing/nightly jobs as a workaround. Verify the
new PR run actually appears before claiming the reporting gap is fixed; if it
needs owner activation, record the exact setting/action rather than bypassing
fork security. No Actions settings or inherited workflows are changed here.

## Lightweight documentation lane

`.github/workflows/fair-bioheaders-docs.yml` runs on every PR to `master`, pushes
to `master` and manual dispatch, with stable job name **FAIR BioHeaders
documentation**. It checks root `AGENTS.md`, this guide and its own checker tests.
It has no workflow-level path filter, so documentation-only PRs receive a result
and recipe PRs receive an explicitly limited documentation result.

```sh
python -m unittest discover -s scripts/fair_bioheaders -p 'test_*.py' -v
python scripts/fair_bioheaders/check_docs.py AGENTS.md docs/fair-bioheaders/ci.md
npx markdownlint-cli2@0.23.2 --config docs/fair-bioheaders/.markdownlint.json AGENTS.md docs/fair-bioheaders/ci.md
```

The Python checker validates whitespace, conflict markers and inline/reference
local file targets, including images, without network access. It does not validate
HTML links, URL availability or fragment anchors. Markdown lint applies only to
the owned files above, not every inherited recipe/document. All checks run with
read-only repository permissions and pinned Actions; no package jobs, registry
credentials, uploads or channel publication are involved.

## Recipe validation remains upstream work

This documentation lane does **not** validate recipes. Do not select it as a
replacement required check for Bioconda lint/build jobs. Branch-protection changes
remain a separate owner action after successful run verification.

Before changing a FAIR BioHeaders recipe, locate the actual package and existing
upstream PR. The fork inspected for this work has no recipe directory named
`fair-bioheaders`, `fhr` or `gff3-validator`; an upstream merge is not automatically
synced into this fork. Do not create a duplicate recipe based on that absence.

Follow `.github/PULL_REQUEST_TEMPLATE.md`, `config.yml` and the current upstream
Bioconda contributor guide. Existing `.github/workflows/PR.yml` documents recipe
lint and platform build commands, including change selection and environment
setup. The important local invocation shapes are:

```sh
bioconda-utils lint --loglevel debug --git-range origin/master HEAD
bioconda-utils build recipes config.yml --help
```

Run these in the reviewed upstream Bioconda environment, not an arbitrary system
Python. Use the exact current upstream change-selection/platform options before
building; the help command above does not execute or verify a build. Check source
artifact hashes, dependencies, licenses and version/build-number rules, then test
installed CLI/import behavior and packaged schema/data. PR checks must not upload
packages. Full scoped recipe lint/build reporting and a safe activation strategy
remain in issue #4; this PR delivers the initial owned-documentation lane only.

Upstream recipe PRs belong at
[bioconda/bioconda-recipes](https://github.com/bioconda/bioconda-recipes).
Fork documentation success is not proof of package availability on the channel.
