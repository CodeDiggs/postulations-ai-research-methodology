# Redaction, selection and exclusion ledger — staging v1

**Scope:** Evidence for the methodology paper, not an archive of all nine scientific investigations. **Repository remains private.** The source repository is a distinct private research workspace.

## Source-equivalent exhibits

Fourteen historical GitHub text documents were staged **without changing their text**, along with the unchanged v3.4 manuscript. Each exact copy's deposited Git blob SHA-1 matches the original file's Git blob SHA-1. The precise source path/ref/blob for each is in [PROVENANCE_MANIFEST.json](PROVENANCE_MANIFEST.json).

**Important limitation:** A byte-identical Git text file is still a primary *repository record*, not proof that the original human conversation happened exactly as later reconstructed, or that a scientific claim was adopted. Links embedded in the text may point back to the **private** original repository and thus remain unavailable to anonymous readers.

No raw third-party data/code/PDF was copied into the new repository. Any scientific-paper discussion within these records is an original *project note* and remains subject to publication and quotation review.

## Material transformed or narrowed

| ID | Released content | Purpose | Omitted or changed | Remaining verification limit |
| --- | --- | --- | --- | --- |
| [E01e](excerpts/E01e-2026-11-19-mathematics-specialist-role-excerpt.md) | Exact-line excerpt from the proposed mathematics specialist directive | Verify identity, restricted role, proposed branch and math-vs-test pivot | All original prompt lines except 1–12, 53–59, 77–78, and 89–91 are omitted; local context/intended mathematical work largely removed | The complete private role document and original author creation action are not independently released |
| [E04b](secondary/E04b-2026-11-17-deidentified-schedule-snapshot.md) | De-identified schedule-state table | Test the *counting and caveats* behind ten enabled hourly paper tasks and unknown delivery | Removed automation/task/run IDs, private destination identifiers, full RRULE start times, prompts, full result bodies, unrelated task records | Underlying selected original scheduler JSON is kept private; published table is a derivative |
| [E04c](excerpts/E04c-2026-11-15-ci-failed-then-passing-log-excerpts.md) | Narrow failing and passing Actions lines | Retain reported software replay failure/recovery without full logs | All job-log lines except failed job 132783927263 lines 135–152 and later passing job 132784233188 lines 135–142; removed ANSI escape formatting | Complete original logs, PR patch, source archives and any independent mathematical replication are not released |

## Deliberate exclusions

- **Private research repository Git history**, including 1,072 branch references counted during the prior risk audit, unrelated drafts, PR conversations, and full Actions logs.
- **Access-bearing external links.** The working Source Intelligence branch has contained an OSF `view_only` parameter in an internal retrieval ledger. That private ledger and the parameter's value were **not transferred**.
- **Third-party human datasets, compiled data, proprietary or restricted PDFs/scripts**, including mixed CC0, CC BY and noncommercial source packages requiring individual release decisions.
- **Original private ChatGPT and separate-service AI conversations**, private Library references and raw participant-generated material.
- **Raw scheduler JSON**, which includes automation and run identifiers. The de-identified derived table is released instead.
- **Full supplementary manuscript**, including its private source register, participant audit, review reconstruction and detailed inventories. It is retained in the author's private Library and the working methodology branch, not yet a safe approved public exhibit.
- **Nine provisional scientific candidate source heads.** The coordinator's cross-paper matrix and checkpoint are retained, but the nine underlying proposals and computations were not copied. The matrix alone does not establish their independent truth.

## Remaining release decisions

1. John approves the exact inventory and whether the complete manuscript (which includes unpublished research context and public citations) can be public.
2. A privacy and citation-rights check of every staged document and the *new repository's own commit history* is performed; simple regex negative matches are not comprehensive.
3. If the paper requires stronger anonymous verifiability, additional primary exhibits are selected under a new review, not bulk-imported.
4. The final public visibility change is separately authorized and followed by an unauthenticated download/read test.

No suppression of relevant negative evidence is intended: unproven, non-adopted and software-failing examples remain present. The limits of unreleased material are prominent in the [claim map](CLAIM_TO_EVIDENCE.md).
