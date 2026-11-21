# Round 16 fork maintenance and audit — 2026-11-20

This fork is an upstream recipe collection. The audit manually reviews owned
FAIR BioHeaders docs/routing/checker code and the existing toolkit recipe, not
every unrelated upstream package. Recipe version/source hash/constraints/tests
remain unchanged; fork/source state does not establish channel publication.
The inherited root README and licenses retain upstream provenance.

Bandit 1.8.6 scans `scripts/fair_bioheaders` with default rules, zero per-file scanner parse errors and three findings. B404/B603/B607 identify the Git subprocess: full 40-hex base/head
values are validated and passed as an argument array without a shell. Git and
the local checkout are the invoking user's trust boundary. Gitleaks 8.30.1 scans
the owned docs/scripts/recipe snapshot and their all-ref Git path history with
redact=100. This explicitly excludes unrelated recipes and un-fetched upstream
history; scoped success is not a federation/global secret clearance.

Zizmor 1.16.3 scans all inherited workflows. It initially identifies 30 findings:
three credential-persistence and three moving-action-tag findings in the scoped
PR workflow are fixed by disabling persisted credentials and resolving the
existing checkout v4/fetch-through-merge-base v1 tags to immutable commits.
Read-only upstream Git discovery still works without stored Git credentials.
No package publishing workflow or repository Actions/protection setting changes.

The other 24 inherited workflow findings remain explicitly outside the owned
maintenance slice: broad workflow permissions, moving action refs and credential
persistence in upstream Bulk/CommentResponder/master/nightly/build-failures jobs.
The template-interpolation warning uses a branch matrix restricted to master/bulk
by its triggers; no attacker-controlled new branch is introduced by this packet.
These are upstream/fork-owner workflow-hardening decisions, not hidden passes or
an invitation to enable inherited publishing jobs. Full redacted location-level
outputs are retained with the coordinator for owner disposition; no new exploit
claim is made in a public issue. The fork maintainer owns which inherited jobs
should ever run here; upstream Bioconda maintainers own upstream changes.

Run the exact docs/routing checks in [ci.md](ci.md). Documentation workflow
success is not recipe lint/build/platform verification; issue #4 and existing
upstream contributions retain those gates. Old no-recipe claims were corrected
against the actual 0.8.1 recipe. Ambiguous historic branches, tags and active
upstream contribution branches are retained. Every PR gets another actual model
review (family diversity preferred); humans alone merge, including upstream PRs.

Reproducible scan shapes (run from the declared repository/source scope):
`bandit -r SOURCE -f json`, `zizmor --format json .github/workflows`,
`gitleaks dir SCOPE --redact=100 --report-format json` and
`gitleaks git . --log-opts=--all --redact=100 --report-format json`.
Bioconda history additionally restricts log paths to owned FAIR docs/scripts and
recipes; scaffold-inapplicable tools are not claimed as passes.
[Redacted source/finding inventory](audit-2026-11-20.json) records actual coverage
and locations. No raw credential values are committed.

Owned tree scan reports zero matches; path-restricted all-ref history covers
27 commits and reports two public accession/SeqCol fixture identifiers. Those
historical fixture bytes are preserved. No authentication credential is found
in that scoped scan. This is not a scan of all upstream recipes/history.
