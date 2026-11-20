# Public-release checklist

**Historical pre-release checklist.** John subsequently authorized publication of this limited new repository and GitHub confirms it is now public as of November 20, 2026. Read [current release status](PUBLIC_RELEASE_STATUS_2026-11-20.md). Outstanding checks below concern external anonymous reachability, publication/rights responsibilities and journal submission—not whether the author has changed visibility.

The original working repository has extensive research history (previous inventory: 1,072 branch refs), third-party source materials under differing terms, private research records, and an access-bearing OSF view-only URL in an internal retrieval log. Those files must **not** be imported automatically.

## Staging actions completed (not release authorization)

- [x] Created an independent private repository without importing the working research history.
- [x] Staged the unchanged v3.4 Markdown manuscript and 14 byte-identical original/secondary documentary records.
- [x] Staged three limited excerpted or de-identified records with an explicit redaction/exclusion ledger.
- [x] Verified 15 exact-copy Git blobs matched their original Git source blobs (14 evidence files and the manuscript).
- [x] Added a claim-to-evidence map, per-file provenance manifest and offline content verifier.
- [x] Ran the existing Python manifest verifier in a fresh GitHub Actions checkout: [successful run](https://github.com/CodeDiggs/postulations-ai-research-methodology/actions/runs/44657237893).
- [x] Ran a stronger, full-reachable-history pattern scan in GitHub Actions: [successful run](https://github.com/CodeDiggs/postulations-ai-research-methodology/actions/runs/44657685421), 37 unique blobs at that commit.
- [x] Conducted a document-level privacy and third-party-asset preflight; no raw third-party datasets, source PDFs, personal-email records or identified access-bearing OSF tokens are staged.
- [x] Author explicitly approved the selected repository's public visibility and completed the GitHub setting change. **Independent legal/IP and individual third-party text-redistribution clearance has not been certified**; see current release status.
- [ ] Test independent anonymous web access; the release is confirmed public by GitHub metadata, but this chat's external web reader returned cache misses.

## Publication/independent verification gates (release already occurred)

- [x] **Author release scope approval.** John approved making this selected new evidence repository public, not the original working repository; the content and publication limitations remain documented.
- [x] **Technical per-exhibit review.** All 18 manuscript/evidence entries have source/deposited blob identities and classification. Additional author publication/IP clearance remains separately required.
- [x] **Bounded secret and privacy screening.** The new repository's tracked text and reachable historical blobs passed the documented pattern scans in Actions; no binary or encoded attachments exist. Search matches are not exhaustive, and this is not a professional forensic audit.
- [ ] **Third-party rights.** Verify license, attribution and redistribution for every copied dataset, table, PDF or script. Prefer linking to original source rather than hosting source bytes; do not transfer one source's CC0/CC BY rights to another.
- [x] **Data minimization.** The new repository contains selected manuscript/evidence text only, with a redaction ledger; the original private history was not imported.
- [x] **Bounded scientific/evidentiary labeling.** The claim map and redaction ledger separate upload, use, adoption and validation and explicitly preserve negative results and source gaps.
- [ ] **Publication disclosure.** Author approves the AI-use and contributions statement appropriate to the chosen venue; current anonymized manuscript is not necessarily venue-compliant.
- [ ] **Intellectual-property decision.** Confirm the planned release won't inadvertently disclose patent-sensitive ideas or other materials whose broader publication is not intended.
- [ ] **Independent access test.** A person without collaborator access opens every purportedly public evidence reference and reports unavailable items. A participant reviewer is not a substitute for independent audit.
- [ ] **License and reuse terms.** Decide whether author-originated text has an explicit license; preserve any separate upstream data/code licenses. Public visibility alone does not confer a license.
- [x] **Public-visibility approval.** John approved the setting change and reported completing it; GitHub metadata independently confirms public visibility. Manuscript *journal-submission* approval is a separate, still-uncompleted action.

See the [final bounded release decision](PUBLIC_RELEASE_DECISION_2026-11-19.md) for the verified checks and remaining author gate.

## Required final outcome

A dated manifest listing **every released file, checksum, source, rights, evidence scope and redaction**; a frozen version of the manuscript; and a clear data-availability statement for external reviewers.

**No visibility changes, privacy settings, deletions, history rewrites, or credential rotations are authorized by this checklist.**
