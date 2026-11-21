# FAIR BioHeaders packaging in this fork

This is a fork of the Bioconda recipe collection, not an installable Python
library or a separate package channel. The inherited root README remains
upstream documentation. For the toolkit use `pip install fair-bioheaders` or
verify the actual package/version on Bioconda before choosing Conda. A recipe
file, fork commit or passing documentation job does not publish a package.

The refreshed source contains `recipes/fair-bioheaders/meta.yaml` at 0.8.1.
Its Jinja version, source URL and SHA-256 select the actual sdist; build number,
runtime constraints, entry points and installed CLI/import tests must agree.
Do not copy a new schema into recipe patches or duplicate an existing recipe.
The upstream 0.13.1 recipe contribution and its external merge/channel gates
remain separate from this maintenance PR.

Start with [CI and scoped recipe validation](ci.md). Important owned helpers:
`classify_changes.py` compares exact full Git SHAs and conservatively routes
unknown/recipe paths through recipe CI; `check_docs.py` checks owned local
Markdown targets/whitespace without networking or anchor checks. Their unittest
suite is run before handoff. Git subprocesses are argument arrays without shell
interpolation; Git executable and checkout are the invoking user's trust boundary.

[Maintenance audit](round16-maintenance.md) records the scope and inherited
workflow findings. Current policy is in [AGENTS](../../AGENTS.md): another actual
model independently reviews every PR and a human alone merges, including
upstream contributions. No uploads, Actions-setting changes, new recipes or
release publication are part of this packet.
