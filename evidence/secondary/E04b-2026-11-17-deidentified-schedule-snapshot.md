# E04b — De-identified research-schedule configuration snapshot

**Classification:** Derived/redacted record from the original selected read-only scheduler extract, **not** raw or complete independent evidence of research execution or delivery.

**Recorded observation:** November 17, 2026, 21:12:35–21:12:54 EST (inventory), 21:14:25–21:14:27 EST (detail inspection). The source itself is a selected extract compiled from earlier read-only calls.

**Source provenance:** `Postulations_Scheduler_Evidence_2026-11-17.json` (author-retained Library; full original **not included**). Manuscript source register [P20] reports SHA-256 `53a89b37a6b056d2d6e818fc60c1ce25a823128f1eb281fbe93c87b534e8826e`; **this source digest is transcribed from the register and has not been recomputed from original bytes in this publication package.** Related contextual audit: [E04a](E04a-hourly-execution-bounded-audit.md).

## Source-bounded task readout

| Stream (role label only) | Configuration | Cadence | Last-run state in inspected detail | Delivery status |
| --- | --- | --- | --- | --- |
| Paper I | Enabled | Hourly | completed | unknown |
| Paper II MAIN | Enabled | Hourly | in_progress | unknown |
| Paper II Postulations2 | Enabled | Hourly | completed | unknown |
| Paper III | Enabled | Hourly | completed | unknown |
| Paper IV | Enabled | Hourly | completed | unknown |
| Paper V | Enabled | Hourly | completed | unknown |
| Paper VI | Enabled | Hourly | completed | unknown |
| Paper VII | Enabled | Hourly | completed | unknown |
| Paper VIII | Enabled | Hourly | completed | unknown |
| Paper IX | Enabled | Hourly | completed | unknown |
| Cross-paper coordinator | Disabled | Hourly | completed | unknown |
| Paper II legacy | Disabled | Hourly | completed | unknown |
| Paper II This Chat | Disabled | Hourly | not inspected | not inspected |
| Research Stream Update Watch | Disabled | Hourly | not inspected | not inspected |

## What the selected source supports

- The captured inventory listed **25 total task records** of various kinds, not 25 scientific streams.
- **Ten active paper-owner tasks** were enabled hourly in the selected November 17 inventory. Paper II has two separate owner research streams.
- The inspected coordinator task was disabled. The record did **not** identify a dedicated Source Intelligence schedule among the 25 results; this is not proof that such automation never existed or ran.
- **Twelve tasks** had detailed snapshots inspected. All twelve listed delivery status as **unknown** in the source extract.
- The newer Paper II MAIN last-run detail was **in progress** at the later read, while an earlier retained output was complete. This does not contradict the earlier handoff snapshot.
- A configured cadence and a recorded completed run do not establish the next conversation received anything, the repository contained the output, or a claim was adopted.

## Redactions / transformations

Only role labels, a binary enabled flag, cadence category, recorded last-run state and delivery state were copied into this table. Removed: automation IDs, run IDs, chat/conversation IDs and destination references, full recurrence definitions (including start times), scheduled timestamps at per-task granularity, full prompts, linked private source URLs and output bodies. Additional unspecified scheduler records were excluded as outside the case scope.

**Validation limitation:** An anonymous reader can verify this published *derived table*, its coherent counting and the explicit caveats. They cannot independently verify each scheduler setting without permissioned access to the retained original and its underlying read-only tool returns. An AI assistant's derivation is not a third-party audit.
