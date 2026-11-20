# Public-release checklist

**Current decision: HOLD.** The author has created a separate private clean-history evidence repository. Creation is not an authorization to publish its contents.

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
- [ ] Obtain author's publication/IP and text-redistribution decision for the exact staged manuscript and exhibits; automated scans cannot grant those rights.
- [ ] Test anonymous access **after** authorized public release; it cannot be verified while the repo is private.

## Required gates before public visibility

- [ ] **Author scope approval.** Confirm the exact manuscript/version and what the public archive is permitted to include; distinguish paper evidence from substantive unpublished research.
- [x] **Technical per-exhibit review.** All 18 manuscript/evidence entries have source/deposited blob identities and classification. Additional author publication/IP clearance remains separately required.
- [x] **Bounded secret and privacy screening.** The new repository's tracked text and reachable historical blobs passed the documented pattern scans in Actions; no binary or encoded attachments exist. Search matches are not exhaustive, and this is not a professional forensic audit.
- [ ] **Third-party rights.** Verify license, attribution and redistribution for every copied dataset, table, PDF or script. Prefer linking to original source rather than hosting source bytes; do not transfer one source's CC0/CC BY rights to another.
- [x] **Data minimization.** The new repository contains selected manuscript/evidence text only, with a redaction ledger; the original private history was not imported.
- [x] **Bounded scientific/evidentiary labeling.** The claim map and redaction ledger separate upload, use, adoption and validation and explicitly preserve negative results and source gaps.
- [ ] **Publication disclosure.** Author approves the AI-use and contributions statement appropriate to the chosen venue; current anonymized manuscript is not necessarily venue-compliant.
- [ ] **Intellectual-property decision.** Confirm the planned release won't inadvertently disclose patent-sensitive ideas or other materials whose broader publication is not intended.
- [ ] **Independent access test.** A person without collaborator access opens every purportedly public evidence reference and reports unavailable items. A participant reviewer is not a substitute for independent audit.
- [ ] **License and reuse terms.** Decide whether author-originated text has an explicit license; preserve any separate upstream data/code licenses. Public visibility alone does not confer a license.
- [ ] **Final author sign-off.** John explicitly approves visibility change, exact manifest and timestamp. The staging assistant must not infer approval from repository creation or a prior broad discussion.

See the [final bounded release decision](PUBLIC_RELEASE_DECISION_2026-11-19.md) for the verified checks and remaining author gate.

## Required final outcome

A dated manifest listing **every released file, checksum, source, rights, evidence scope and redaction**; a frozen version of the manuscript; and a clear data-availability statement for external reviewers.

**No visibility changes, privacy settings, deletions, history rewrites, or credential rotations are authorized by this checklist.**
