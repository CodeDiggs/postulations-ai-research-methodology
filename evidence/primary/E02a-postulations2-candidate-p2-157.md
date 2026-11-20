# P2-157 — Exact all-lag observational equivalence under unknown input/readout mixing

**Status:** non-authoritative independent Postulations2 adversarial investigation for Issue #26. This is not a new investigation ID, and not Main Paper II evidence/adoption.

## Question and conditional mathematical result

For stable two-state physical dynamics `J=[[a,K],[beta,rho]]`, `K=(1-a)s` (normalized illustrative mapping), `L=K beta`, `tau=a+rho`, `Delta=a rho-L`, consider physical lag-rise margin `R=L-a(1-a)`. Holding the two pole invariants `tau,Delta` fixed gives `R=a(tau-1)-Delta`. Thus the same poles can coexist with opposite physical rise signs by changing physically labeled `a`.

Let `J0=[[2/5,3/20],[5/3,1/5]]`, `J1=[[1/2,1/8],[44/25,1/10]]` (`s=1/4` for both). They share `tau=3/5`, `Delta=-17/100`, Jury margins `23/100,143/100,117/100`, and positive physical normalizations, yet `R0=+1/100`, `R1=-3/100`.

Define `T=[[1,3/50],[0,132/125]]`, `B0=I`, `C0=[1,0]`, `B1=T B0`, `C1=C0 T^-1=[1,-5/88]`. Exact rational algebra verifies `J1=T J0 T^-1`, hence **`C1 J1^n B1=C0 J0^n B0` for every n, all linear H/A histories**. The first four observed H lags of *both* models are `[1,2/5,41/100,157/500]` (apparent rise at lag 2), while the physical selective H lags of J1 begin `[1,1/2,47/100,...]` (physical nonrise). Observed A lags also match.

The alternative has small, fixed A-to-p leakage `3/50=0.06`, A-to-z gain `132/125=1.056`, and z-to-report readout mixing `-5/88≈-0.05682`; H itself stays selective. Both candidates belong to the *same allowed model family* of two physical states and unknown constant B/C, rather than competing classes with artificially unequal state capacity. They do not have the same *nuisance parameter values*, and the second needs calibration flexibility. Independent exact selective B/C anchors remove this specific ambiguity.

## Arbitrarily weak mixing near the boundary

With fixed `tau=3/5,Delta=-17/100,s=1/4`, the physical rise boundary occurs at `a*=17/40`. Choose `a0=a*-eps` and `a1=a*+eps`. Then `R0=(2/5)eps`, `R1=-(2/5)eps`. For `beta_i=[a_i(tau-a_i)-Delta]/[(1-a_i)s]`, the upper-triangular `T=[[1,(a1-a0)/beta0],[0,beta1/beta0]]` conjugates the plants and tends to I as `eps→0`. Thus arbitrarily small unknown B/C mixing can defeat **sign-only** identification near the physical boundary, even with noiseless all-lag two-channel measurements. This is a conditional theorem about representation and observation, not proof of a novel human mechanism.

## Actually executed check and reproducibility

Command: `python experiments/p2_postulations2/mixing_witness.py` (Python stdlib only, no seed or stochastic simulation). Exactly checks lag indices 0–32 for the reference and two near-boundary witnesses (eps=1/10000 and 1/1000000), 99 exact rational two-channel response comparisons, all similarity identities, Jury margins and rise signs. Output: `runs/P2-POSTULATIONS2/2026-11-10/mixing_witness_result.json`. Original executed working source SHA-256 `c9c17d7c5c35da756fcb656d3b93e5c72ce79418e784dcb50f804ab57152743d`; result SHA-256 `797db259c3fac2050de9475961d1681c94fd3622b0cfb54815f6142a01b45841`. Their Git blob SHA values match the working file bytes. Initial compact reimplementation had an internal double-application of B1 and failed an assertion; corrected the starting matrix to identity, then the stated check passed. A separate longer predeclared exact-rational audit also passed; this committed version is the smaller replayable test.

**Limitations:** Similarity transforms alone do not establish different observables or causal mechanisms; the physical state interpretation requires externally anchored state/intervention/readout definitions. Equal mathematical order is not independent evidence against adaptation, feedforward, criterion-drift or reporting alternatives. The near-boundary effect is arbitrarily small. The observed response does **not** identify physical `a,L,rho` without input/output calibration, and `h0–h3` recovery only applies to calibrated selective H. No human validation, unique physical Dynamic Door mechanism or general subjective theory proof.

No Main H×A×lags 0–15 design/allocation change, H1 activation, delta-star/pi-star commitment, inference-budget change, recruitment, ethics or consent approval. P2-264, X-169/X-171 source gaps persist. **No finite experiment can definitively prove an unrestricted theory of subjective experience.**
