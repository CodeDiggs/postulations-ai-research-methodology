# Evidence packet — retrospective methodology paper v3.4

**STATUS: PRIVATE STAGING. PUBLICATION IS NOT AUTHORIZED.**

This is an intentionally bounded archive of the original research **organization**, not an attempt to validate the nine scientific Postulations hypotheses. It keeps the underlying working repository's Git history and raw research datasets private.

## Start here

1. [Claim-to-evidence map](CLAIM_TO_EVIDENCE.md): match a manuscript statement to the exact documentary exhibit and see what is still unknown.
2. [Machine-readable provenance manifest](PROVENANCE_MANIFEST.json): for every copied document, its source path, original Git blob SHA-1, deposited Git blob SHA-1, classification, and modification status.
3. [Redaction and exclusion ledger](REDACTION_AND_EXCLUSION_LOG.md): what was removed or withheld, why, and how that affects external verification.
4. [Public-release checklist](../PUBLIC_RELEASE_CHECKLIST.md): rights, privacy, author signoff, and anonymous-access gates.
5. [Offline verifier](../tools/verify_evidence.py): after cloning or downloading the **new** repository, run `python3 tools/verify_evidence.py`. This verifies the local files' Git blob hashes and screens several common high-risk patterns. It is not a comprehensive secret or rights scan.

6. [Staging QA report](STAGING_QA_REPORT.md): which integrity and exposure checks were actually performed, including their limits.

## Evidence contents

| Family | Records | Documentary question |
| --- | --- | --- |
| [E01](primary/E01a-2026-11-15-owner-branch-registry.md) and [E01e](excerpts/E01e-2026-11-19-mathematics-specialist-role-excerpt.md) | Original owner registry, Source Intelligence instructions, falsification-first policy, coordinator checkpoint, and narrow later math-specialist excerpt | How were scientific paper responsibilities and support functions specified? |
| [E02](primary/E02a-postulations2-candidate-p2-157.md) | Postulations2 P2-157 proposal and Paper II MAIN P2-426 owner decision | Did an auxiliary research stream generate a proposal distinct from owner scientific adoption? |
| [E03](primary/E03a-source-intelligence-r4-dossier.md) | R4 source dossier, P2-464 physical STOP, P2-465 owner assessment and source ledger, and ten-branch delivery ledger | Was source information used while an independent physical inference remained blocked? |
| [E04a](secondary/E04a-hourly-execution-bounded-audit.md), [E04b](secondary/E04b-2026-11-17-deidentified-schedule-snapshot.md), [E04c](excerpts/E04c-2026-11-15-ci-failed-then-passing-log-excerpts.md) | Bounded later audit, de-identified schedule states, selected Actions failure/passing lines | How do configured schedules and software status differ from delivery and scientific adoption? |
| [E05](secondary/E05a-nine-paper-candidate-matrix.md) and [checkpoint](primary/E05b-2026-11-15-nine-paper-checkpoint.md) | Original nine-paper coordination checkpoint and later cross-paper document matrix | Do all nine paper streams have a sampled candidate with explicit limitation/negative-rival status? |

At staging, **14 documents and the manuscript** were exact-byte copies verified to have matching Git blob hashes. **Three** other exhibits are selected, edited or de-identified records. The exact source text of the three edited records cannot be reconstructed solely from this packet.

## Important limits

The source Git blob identity verifies the copied *repository text*, not the original private human-AI conversation, calculations, causal effectiveness, the validity of a postulation, or scientific adoption. The selected scheduler table is not the original scheduler service response. The nine-paper matrix is a purposive coordinator audit and the underlying nine science PR sources were not mirrored here.

Some verbatim historical documents link to the **private working research repository**, so those historical outbound links may remain unavailable to an unauthenticated reader. The relevant excerpted material in this evidence packet is linked internally through the claim map; external access must be checked separately.

Not staged: private conversation exports, library-only files, raw third-party human datasets, uploaded research PDFs, private OSF view-only URLs, original Git commit history, full AI review transcripts, or the complete methods supplement.

**Evidence release only occurs when the author explicitly approves the final inventory and repository visibility change.**
