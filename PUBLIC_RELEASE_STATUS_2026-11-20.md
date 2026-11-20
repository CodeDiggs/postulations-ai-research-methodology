# Public evidence release status — 20 November 2026

**Repository:** [CodeDiggs/postulations-ai-research-methodology](https://github.com/CodeDiggs/postulations-ai-research-methodology)  
**Current visibility:** **PUBLIC**, confirmed from GitHub repository metadata on 20 November 2026.  
**Scope:** A deliberately restricted documentary evidence release for *Human-Initiated Multi-AI Research Coordination in the Postulations Project*, manuscript v3.4. **This is not journal publication or scientific validation.**

## What changed

John Giles explicitly agreed to make **this newly created methodology repository** public and then reported completing the GitHub visibility change. GitHub now returns `visibility: public` for this repository.

The separate, original [Postulations / Dynamic Door working research repository](https://github.com/CodeDiggs/postulations-dynamic-door) was independently checked and **remains private**. It was not forked or copied wholesale.

## Release contents

- [Manuscript v3.4](manuscript/Postulations_AI_Methodology_Manuscript_v3_4.md), an exact Git blob copy of the working source.
- [Evidence guide](evidence/README.md) with source-to-claim links.
- [Provenance manifest](evidence/PROVENANCE_MANIFEST.json), with 14 exact-copy evidence files, three selected/derived exhibits, and the manuscript.
- [Redaction and exclusion ledger](evidence/REDACTION_AND_EXCLUSION_LOG.md).
- [Verifier](tools/verify_evidence.py), which checks the locally downloaded bytes against the manifest.

Earlier [pre-release assessment](PUBLIC_RELEASE_DECISION_2026-11-19.md) and [staging QA report](evidence/STAGING_QA_REPORT.md) are retained as dated history; their statements that the repo was private apply to when they were authored. The manifest's `visibility_at_preparation: private` and `public_release_authorized: false` are also **historical preparation fields**, not an assertion about today's visibility.

## Verification status

The [last confirmed pre-release GitHub Actions run](https://github.com/CodeDiggs/postulations-ai-research-methodology/actions/runs/44658076406) passed the 18-entry manifest check and limited full-reachable-history pattern scan. It does not certify privacy, reuse rights, or validity of the underlying scientific papers.

- **GitHub public visibility:** confirmed by repository metadata.
- **File paths and source Git blobs:** checked with the repository connection.
- **Direct anonymous external-page retrieval:** **not verified** as of this record. The unauthenticated web fetch service returned cache misses for the newly public repository, and the local container lacked external DNS/network access. Thus this record does *not* assert that an unauthenticated outside browser successfully opened every link.
- **Historical original records:** many source links still point to a private working repository. The copies within this public repository preserve selected text but do not expose the complete source history.
- **Independent human audit:** not conducted.

## Publication boundaries and next steps

A public documentary evidence snapshot is **not** a journal submission, institutional ethics approval, physical demonstration of the Dynamic Door hypothesis, or a causal test showing multi-AI research outperforms alternatives. The case study's unpublished content and journal disclosure obligations remain the human author's responsibility.

1. Confirm actual unauthenticated reader access when a non-signed-in browser can fetch this new repository; record results without pretending the current cache failure is a true access denial.
2. Prepare venue-specific keywords, AI-use disclosure, data availability, affiliations, funding/conflicts/ethics statements and a submission cover letter; author reviews and approves those.
3. If required by the journal, arrange a controlled outside human verification of the original private scheduler, historical conversation and reviewer sources.
4. Do not silently publish the complete private provenance supplement, source research datasets, or remaining nine-paper research history.

**No change was made to the original scientific research repository or its schedules in connection with this visibility confirmation.**
