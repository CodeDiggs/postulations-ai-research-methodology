# Private evidence-package staging QA — 2026-11-19

**Repository:** `CodeDiggs/postulations-ai-research-methodology`  
**Current authorization:** Private staging only. The author has **not** authorized changing visibility.  
**Manuscript:** v3.4. No scientific papers, current working repository branches, or automations were modified during evidence staging.

## Checks performed and outcomes

| Check | Result | Meaning / limit |
| --- | --- | --- |
| New repository separation | **PASS** | New repository has only `main` as inspected; no fork relation/imported original Git history |
| Current-file inventory at QA checkpoint `06b0125df63ce0c56cc637587dacd59293cc5519` | **PASS** | 26 files: 23 Markdown, 1 JSON manifest, 1 Python script, 1 `.gitignore`; no PDFs, archives or raw source datasets |
| Exact-byte source preservation | **PASS — 15/15** | Fourteen staged documentary evidence files and unchanged v3.4 manuscript have identical destination/source Git blob SHA-1 |
| Manifest to staged files | **PASS — 18/18** | 14 exact-copy evidence files + 3 transformed/selected exhibits + manuscript exist with matching recorded deposited blob IDs |
| Current-file high-risk pattern screening | **NO MATCHES — 26/26** | Pattern checks for GitHub token formats, PEM private-key headers, OSF view-only parameter values, private ChatGPT Library links, and email-like strings. This is not a full credential/privacy scanner |
| Historic patch screening of **new** repository | **NO MATCHES — 32/32 commits** | Sampled all 32 then-existing commits; each returned a patch for its changed file; no matches for the same pattern families. These checks cover the staging repo only, not the 1,072-branch original |
| Reviewer-facing Markdown links | **PASS — 47/47** | Relative links in README, evidence guide, claim map, redaction log and checklist resolved to existing tracked files as of checkpoint. Embedded links in copied historical records may still point to private original sources |
| Access-control state | **PASS — PRIVATE** | The GitHub repository remained private through these checks |
| Anonymous independent access | **NOT PERFORMED** | Cannot test a genuinely anonymous reviewer until a separate public release is approved |
| Offline Python verifier end-to-end run | **NOT PERFORMED** | `tools/verify_evidence.py` was committed for external replay; within this connector-based staging session, no local authenticated clone was executed |
| Independent human documentary/rights audit | **NOT PERFORMED** | Author/source permissions and licensing remain approval gates |

## Exact exhibits and evidence strengths

- **Primary and unchanged:** original branch-ownership and Source Intelligence instructions, falsification policy, coordination checkpoint, a Postulations2 candidate, Paper II MAIN decisions, source dossier and source ledger, R4 distribution report, and the nine-paper coordination checkpoint. Git blob identity authenticates *these repository documents*, not every historical chat or the scientific claims.
- **Secondary and unchanged:** bounded hourly-execution audit and the nine-paper candidate matrix; coordinator-authored retrospective analysis, not independent experiment replication.
- **Derived / selected:** mathematics-role original-line excerpt; a de-identified private scheduler extract; selected Actions failure/recovery log lines. Their source contents were **not** fully reproduced.
- **Not included:** raw human source datasets, private/embargoed-view OSF access parameters, private conversation transcripts, original Git history, complete UQCP reviewer record, full methods supplement, raw scheduler JSON, the nine original scientific candidate source heads and their code.

## Remaining factual limitations

1. The original 10 hourly tasks were read from a bounded scheduler extract. The public-facing table does not independently authenticate the scheduler's private raw tool returns; all 12 detailed delivery states were unknown.
2. Source and GitHub handoff claims demonstrate selected document deposits and owner responses. No nine-paper-wide causal or effectiveness denominator exists.
3. The original research repository is still private. Public readers will not be able to click historical links into that repository or confirm its original commit history without access; the mirrored text is present and internally content-verified.
4. The cross-AI UQCP reviewing case, original author chat history and the full evidence supplement are not independently inspectable through this public-design snapshot. Preserve these gaps explicitly in the paper's data-availability statement.
5. The new repository's present files were screened by limited expressions; privacy, third-party copyright, and intellectual-property publication decisions still require human review.

## Final release path

1. Author checks the [claim map](CLAIM_TO_EVIDENCE.md), [manifest](PROVENANCE_MANIFEST.json) and [redaction/exclusion ledger](REDACTION_AND_EXCLUSION_LOG.md).
2. Confirm rights, privacy and intellectual-property policy for the **exact staged 18 manuscript/evidence files**, plus supporting README/checklist/script. Do not add source data indiscriminately.
3. Complete a local verification run (`python3 tools/verify_evidence.py`) and, if desired, a separate human documentary review.
4. Obtain explicit approval to change visibility. Until then, keep the repository **PRIVATE**.
5. Only after a public visibility change, use an unauthenticated session to test every public citation and release an immutable publication snapshot or tag as appropriate.

**Decision:** Staging has passed its bounded technical integrity checks. **Public release remains HOLD pending author approval and outstanding rights/privacy review.** No destructive actions, branch changes in the original repository, automation edits or visibility changes occurred.
