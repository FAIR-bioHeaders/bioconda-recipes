# Agent instructions

## Repository context and scope

This is FAIR-bioHeaders' fork of upstream bioconda/bioconda-recipes, based on
`master`. Preserve upstream contribution, recipe, licensing and CI conventions.
The guidance below concerns FAIR BioHeaders maintenance in this fork; it does
not impose FAIR BioHeaders governance or schema policy on unrelated packages.
Do not merge a specification repository into this recipe tree.

Inspect README and the relevant recipe's `meta.yaml`, patches, tests and upstream
release before changing packaging. FAIR BioHeaders schema design belongs in the
specification repositories, not recipe patches. Package adopted upstream behavior
and document actual supported versions. Keep source URLs, hashes, build numbers,
dependencies, licenses and installed-command tests consistent; use documented
Bioconda checks for recipe changes. An AGENTS.md-only PR changes no recipes and
needs `git diff --check` and guidance review rather than a package rebuild.

## Schema additions and their own development cycle

A new optional field, structured alternative, enum value, constraint, required
field or changed meaning is a schema-contract change, even when motivated by a
UI, exporter, parser fix or documentation task. Identify it explicitly as a
**schema addition** or other contract change in its issue and PR. Supporting an
already adopted field in a consumer is implementation work, not a new field.

Schema additions have their own proposal, review, compatibility, versioning and
release cycle. Keep them separately reviewable from routine fixes, website work,
packaging and dependency updates; link dependent implementation PRs rather than
silently adopting a field downstream. Shared fields/objects and cross-type rules
belong in FAIR-bioHeaders-Specification; type-specific design starts in the owning
development repository and is coordinated into shared publication. Name affected
types, requiredness, semantics, mappings, serializers and conformance fixtures.

During active construction of FHP, FHT and FHGFF3, maintainers may iterate on draft
fields with lighter process and include coordinated schema/implementation work in
one clearly scoped PR. Record the proposal and compatibility impact in that PR;
this flexibility does not make every field adopted or supported. Preserve already
published contracts and cited versions, label draft behavior, and obtain joint
maintainer review before publication. FHR additions retain the separate cycle.
Do not apply draft flexibility to released FHP/FHGFF3 schemas retroactively.

Use the shared specification's `docs/SCHEMA-VERSIONS.md` and
`schemas/versions.json`: contract versions are per type, distinct from repository
release tags and biological resource versions. Additive changes that preserve all
valid values and meanings qualify for a minor increment; invalidating records or
changing meanings requires a major increment. Do not assign a new version merely
for implementing an existing contract. Never rewrite immutable releases, fixed
schema aliases or existing file-bound headers as incidental cleanup. Header edits
require checksum recomputation and may affect downstream parent links.

Check the adoption decision and released support before implementing a proposal;
an issue or PR's existence does not establish adoption. Structured vouchers
(FAIR-bioHeaders-Specification#139/#140) and mapping profiles (#56 in that same
repository) have their own review history. Implemented subsets do not establish
full profile or header-family support. The mapping page tracked in
fair-bioheaders.github.io#29 depends on approved profiles. Recheck these records
rather than relying on a copied description of their temporary status.

## FAIR BioHeaders recipe handoff

Before editing, locate the actual recipe for the released distribution and check
upstream bioconda/bioconda-recipes and any existing recipe PR. Do not assume a
recipe named `fair-bioheaders`, `fhr` or `gff3-validator` already exists in this
fork: the reviewed tree had no matching recipe directory. Establish ownership and
current upstream state rather than creating duplicate packages from this note.
Changes to this fork are reviewed locally; publication to the Bioconda channel
requires the appropriate upstream PR/merge and build, not a merge here alone.

Follow `.github/PULL_REQUEST_TEMPLATE.md`, `config.yml` and the current upstream
recipe guidance. For an existing version's packaging/dependency change, increment
the build number; for a new version normally reset it to zero. Update source
hashes from the actual released artifact, preserve applicable licenses and test
installed imports/CLI behavior and required package data. Do not package an
unadopted schema through a downstream patch or infer that a compatibility
package's historical name is the current distribution name.

The PR workflow uses `bioconda-utils lint --loglevel debug --git-range
origin/BASE HEAD` (one command, substitute the actual base) and platform build jobs
with `bioconda-utils build recipes config.yml`. Follow the exact change-selection,
platform and artifact options in `.github/workflows/PR.yml` and upstream guidance
before running a build; do not launch the whole recipe collection for a one-recipe
change. State which package/platform tests ran. Guidance-only changes need no
recipe build or upload.

## Fork documentation CI

`docs/fair-bioheaders/ci.md` records the observed workflow activation gap and the
new lightweight documentation lane. Run its exact commands for owned Markdown
and `scripts/fair_bioheaders/` tests. Its result is not recipe lint/build coverage;
keep issue #4 open for real recipe/platform verification of the scoped lane. Check that
the new workflow actually reports a PR result before claiming activation worked.
Do not enable inherited publishing jobs or change branch protection as a shortcut.

## Issue, project and code-review behavior

### Issues and the connected project

- Add every issue you work on to the connected project (project #9, "FAIR
  BioHeaders — 2026 refresh") and set `Status` to `In Progress` when work starts.
- Keep `Status` current as the work moves (`Todo`, `In Progress`, `Blocked`,
  `Blocked - In Progress`, `Done`), and set `Outcome` when it closes.
- Link every PR to its issue (`Closes #N` or `Refs #N`). Do not do unreported work.
- After each work run (implementation, tests, review pass), post a status comment
  on the issue or PR: what changed, checks run and results, commit/PR links,
  blockers, and the next action. Do not rely on chat history.

### Code review on a PR

When a PR receives code review (human or Copilot):

1. Read the overall review and every inline comment before changing anything.
2. Make each fix in a **new commit**. Do not amend or force-push over reviewed
   commits; if a rebase is required, cite the new head in the replies.
3. Reply to each inline finding with the fix and the relevant commit hash.
4. Resolve that inline comment/thread.
5. After all findings are handled, post an overall reply to the review
   summarizing each finding's disposition and the commits.
6. Treat optional suggestions as required unless they are genuinely out of
   scope; state why and link a follow-up issue.

Do not push to a repository's main branch or merge a PR without maintainer
approval.
