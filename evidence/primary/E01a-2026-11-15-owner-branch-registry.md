# Permanent Git branch ownership — v1 (2026-11-15)

**User-directed operating rule:** **ONE persistent owner branch per originating research chat/stream, not a new branch for every scheduled research iteration.** All streams use the already-existing private repository `CodeDiggs/postulations-dynamic-door`; no new GitHub repository is required. Historical research source identities, scientific acceptance and chat ownership remain unchanged.

## Stable branch registry

| Research owner (one independent originating conversation) | Permanent writable branch | State |
|---|---|---|
| Cross-Paper Research Coordination (originating chat) | `streams/cross-paper-coordination` | Active; create once |
| New **Research Documentation & Source Intelligence Coordinator** | **`streams/source-intelligence`** | **New chat creates its own branch exactly once** |
| Paper I — UQCP MAIN | `streams/paper-i-main` | Active |
| Paper II — authoritative MAIN | `streams/paper-ii-main` | Active |
| Paper II — independent IND | `streams/paper-ii-ind` | Reserved; create only when originating IND chat works |
| Paper II — Postulations2 | `streams/paper-ii-postulations2` | Active; automation titled “Independent Paper II Research” is **Postulations2**, not IND |
| Paper II — MAIN-legacy | `streams/paper-ii-main-legacy` | Reserved; schedule disabled; do not resume |
| Paper III — experiential possibility | `streams/paper-iii-main` | Active |
| Paper IV — Dynamic Accessibility | `streams/paper-iv-main` | Active |
| Paper V — Memory | `streams/paper-v-main` | Active |
| Paper VI — Collective Perception | `streams/paper-vi-main` | Active |
| Paper VII — Collective Influence | `streams/paper-vii-main` | Active |
| Paper VIII — Informational Foundations | `streams/paper-viii-main` | Active |
| Paper IX — Physical Actualization | `streams/paper-ix-main` | Active |

**Each branch identifies the actual source chat**, not merely the paper topic, the automation title, an hourly run, or a stale GitHub PR. New independently owned chats require an explicit new stable name and registry review before creating branches. Do not reuse another owner's permanent branch.

## Required behavior for EVERY owner chat / automation

1. **Read current `main` governance first:** `AGENTS.md`, this branch registry, paper INTERFACE, falsification-first protocol and relevant open original PRs. Confirm the owner/stream identity and exact assigned branch.
2. **Verify branch:** use the exact assigned permanent branch. If it is missing, create it **once from current `main`** (never create a replacement on every run); if present, read its current head and continue there. **Do not reset, force-push or overwrite it**, and do not silently mix source histories.
3. **Routine work:** commit the iteration's source, research note, data/code, tests and provenance directly to its own persistent branch, using versioned paths and unique research IDs rather than new per-run branches. Read and verify the current branch head before each write to avoid clobbering another commit. A write to another stream branch or `main` is forbidden except an explicitly approved integration.
4. **When temporary isolation is genuinely necessary:** create no more than the smallest necessary temporary branch from **its own permanent branch**, using `work/<owner-slug>/<specific-purpose>`. Its GitHub PR must target **the owner's permanent branch**, NOT `main`. After verification and review, merge/cherry-pick eligible work **back into that owner's branch**. Only then may a temporary branch be closed/deleted after preserving original hashes and history. A temporary branch must not become a new authoritative stream or indefinite replacement. If isolation is unnecessary, do not create it.
5. **Integration to `main` is exceptional:** `main` is the governance/explicitly reviewed integration record. A passed CI check, mathematical theorem, deterministic simulation or owner-branch merge **does not** adopt a claim. Scientific integration requires paper-owner scientific review, provenance, adverse rivals, explicit adopted-state change and approval. Prepare a separate, minimal, reviewable integration PR from a reviewed subset rather than merging the entire accumulating owner branch indiscriminately.
6. **Existing PRs and proliferated branches:** hundreds of earlier branches/PRs may predate this policy. **Do not delete, bulk-merge, rebase, retarget or close them automatically**. Inventory them in the owning stream, selectively import original source artifacts into the owner's stable branch only after provenance/reproducibility review, and track the old URLs/SHAs as historical source records. No claim that all older research has already been imported.
7. **CI reality:** the existing `.github/workflows/checks.yml` triggers on `main` pushes and `pull_request` events. **A direct push to `streams/*` does NOT currently run GitHub Actions automatically.** Do not claim a green Actions run for direct stream commits. Run permitted local tests and record hashes/command outputs; when remote CI is needed, use at most **one maintained draft PR per permanent stream targeting `main`** solely as a CI/review surface, NEVER auto-merge it. An optional temporary feature PR targeting the owner's permanent branch also triggers existing PR checks. Do **not** alter workflow triggers, billing, runner settings or spending limits without separate user approval.
8. **Chat and schedule boundaries:** GitHub notes/PR comments do **not** deliver to another ChatGPT chat by themselves. Keep user-facing updates in the originating chat; preserve active task cadence, conversation destination and disabled status. New source-intelligence chat does not control other paper task schedules.
9. **Scientific focus:** each paper retains its independently falsifiable central question and the [falsification-first protocol](falsification-first-protocol-v1.md). A persistent branch is an organizational tool, not a new scientific premise, claim of originality or evidence of mechanism.

## First-time migration / source continuity

- On the next iteration, each active stream verifies/creates the one permanent branch, writes a small `coordination/streams/<owner-id>.md` identity/handoff record **on that branch only**, and locates its latest two source-owned experiment PRs.
- **Do not copy all earlier experiments automatically.** Make a provenance-preserving list of outstanding candidate PRs and selectively consolidate only one reviewed necessary continuation into owner branch when useful. Keep existing source PRs intact until owner-led reconciliation.
- The Source Intelligence Coordinator should create **`streams/source-intelligence` itself**, from latest `main`, add `coordination/source-intelligence/README.md` and source registry there, then work solely in that branch. Send evidence handoffs as comments/Issues to the relevant source paper. It never pushes research claims or files to paper owners' branches without review.
- New owner branch names must be decided *before* creating the chat's first experimental branch. Avoid creating a separate repository, branch or PR for each literature search, run or source item.

## Accountability checkpoint

Each research run must identify `OWNER_BRANCH`, `OWNER_BRANCH_HEAD`, `EXTRA_BRANCHES_CREATED` (normally zero), destination for any temporary merge and `CI_STATUS` (green/failed/not-run). Include **Decision progress** and the observable test that would change the restricted theory, as previously required. **Branch count is not research progress.**
