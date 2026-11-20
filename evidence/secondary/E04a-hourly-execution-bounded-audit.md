# Hourly research schedule — bounded execution-to-artifact audit

Inspection: 2026-11-18 (America/New_York). **This is a two-window methods audit, not uptime monitoring, a full history, or a measured productivity rate.** No automation configuration was changed.

## Sources and observation boundaries

1. [Original scheduler evidence extraction](https://github.com/CodeDiggs/postulations-dynamic-door/blob/research/ai-methodology/ai-methodology/coordination/pilot-coding-protocol-v1.md) is separately retained in the companion methods workspace as `Postulations_Scheduler_Evidence_2026-11-17.json`. It records a November 17, 2026 21:12–21:14 EST snapshot from automation inventory/detail reads; the linked protocol is the methodology context, **not** a hosted copy of the JSON. Direct JSON was analyzed in this audit.
2. Live private automation peeks on November 18, 2026 for **Paper II MAIN** and **Paper VII** provided the most recent run/result metadata. These later peeks are point observations, not the intervening complete hourly log.
3. An exact GitHub read independently confirmed a linked Paper VII A56 note and JSON under commit `674dbbfd8182f499b27e14f5a6a5cdc5274f8565`. This does not establish correct chat delivery or reproduce its original data analysis.

## November 17 scheduler snapshot

- **Ten** enabled paper-owner tasks were listed: Paper I, Paper II MAIN, Paper II Postulations2, and Papers III–IX. That is ten task streams across nine scientific papers, **not** ten different papers.
- The selected latest-run details showed **nine completed** and **one in progress** (Paper II MAIN) at the detail observation window. Completion is a scheduler status, not confirmation of useful work or message delivery.
- The same audit listed four relevant disabled tasks, including an older cross-paper coordinator and Paper II legacy/duplicate tasks. These were observed disabled, not deleted or never run.
- All ten selected active task details recorded `delivery_status: unknown`. This field is not evidence of delivery failure; it is simply insufficient to certify recipient receipt.
- At least five selected `started_at` timestamps preceded their nominal `scheduled_for` value (Papers IV, V, VI, VII, IX). Scheduler semantics, retries, and clock behavior were not resolved; consequently start-minus-scheduled intervals should not be interpreted as latency in this sample.
- In the retained output samples, MAIN P2-465 and Paper VII A56 contained GitHub links and explicit statements that remote CI was not run. The Paper II legacy sample reported an original-chat delivery failure. None of these three purposefully selected samples supports a general delivery-failure frequency.

## November 18 live spot checks

| Stream | Readout in private peek | Retained report | Limit |
| --- | --- | --- | --- |
| Paper II MAIN, task `Automation_d1453ccb41608191980c68af5164a9a2` | Run `f30b2120-7548-8327-adb6-96df67c12090` scheduled 19:58:05Z; started 19:55:13Z; recorded completed 20:06:29Z | Retained latest response headed **P2-484**, describing a conventional-model identifiability limit and blocked DD empirical validation | Delivery status unknown. No independent source/code replay or review/adoption audit of P2-484 in this note. |
| Paper VII, task `Automation_6190624fafd881918e5092fad0270570` | Run `5740d9be-2acc-8320-9fd1-d42621b61e5b` scheduled 20:24:36Z; started 20:24:48Z; still in progress at peek | Previous latest response headed **A73**, summarizing a thesis-based human-evidence limitation and continued DD mechanism block | Current in-progress run is not a failure. Delivery status unknown. A73 source execution and adoption were not independently audited. |

The later task readout shows the original November 17 snapshot cannot be treated as persistent current state.

## Artifact spot check — earlier Paper VII A56

The November 17 scheduler-retained A56 response linked:
- [Paper VII A56 note](https://github.com/CodeDiggs/postulations-dynamic-door/blob/674dbbfd8182f499b27e14f5a6a5cdc5274f8565/papers/VII/notes/p7_main_20261117_papa_retention_alternative_coding_a56.md), directly fetched (blob `23216d06d9b6fa4f6951c41f4b87bcaeea20ac30`).
- [A56 result JSON](https://github.com/CodeDiggs/postulations-dynamic-door/blob/674dbbfd8182f499b27e14f5a6a5cdc5274f8565/runs/paper-vii-main/p7_main_20261117_papa_retention_coding_a56.json), directly fetched (blob `cb5ce59d488e8e9d14f6bfbca744da922f1ce4a4`).

The files report 1,344 original human-trial rows, six candidate recodings, and 49 inconsistencies that remain unresolved. They classify the exercise as a retrospective raw-data coding audit, not a decisive test of the proposed collective-history mechanism. **Directly verified here:** the linked artifact files and self-reported analysis contents exist at a fixed source head. **Not verified here:** independent recomputation against original source bytes, source-owner review, manuscript uptake, or delivery to the named ChatGPT conversation.

## Audit model and next data requirements

For each predeclared eligible task-hour, record separately:
`task_id | nominal_slot | run_id | recorded_status | result_id | result_retained | source_commit | exact_artifact_paths | CI_state | recipient_identity | receipt_evidence | review_decision | scientific_adoption | missingness_reason`.

Do not infer task creation dates from DTSTART; do not divide selected GitHub links by the ten task inventory records to calculate an effectiveness rate. Before estimating throughput, retrieve a complete fixed-duration run history and GitHub event log, freeze the denominator including failed/missing/no-update slots, cluster multi-chat tasks, and adjudicate every state blind to the producing condition. A code artifact can be real while its scientific assertion remains conditional or unverified.

**Conclusion:** hourly configuration, at least some completed scheduler results, and source-linked GitHub artifacts are documented. Reliable delivery, review, adoption, and causal improvement over simpler workflows remain unmeasured.
