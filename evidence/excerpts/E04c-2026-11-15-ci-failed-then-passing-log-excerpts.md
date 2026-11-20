# E04c — Selected CI failure and recovery log lines

**Scope:** Direct excerpts from the original GitHub Actions job logs, selected for the *same-source replay* case. These are copied log lines, not a new execution or complete reproduction. Whole job logs and archive outputs are deliberately excluded; outside readers cannot authenticate private original jobs without permissioned access.

## Failed first replay

GitHub original run ID: `43704954000`; job ID: `132783927263`. Source URL (may be private): https://github.com/CodeDiggs/postulations-dynamic-door/actions/runs/43704954000

Original job-log lines 135–152, line numbers added; terminal ANSI colors removed:

```text
135 | 2026-11-15T10:37:14.9336893Z test_archived_hashes (test_p2_postulations2_multicell_2035.CheckP22035.test_archived_hashes) ... ok
136 | 2026-11-15T10:37:14.9341043Z test_record (test_p2_postulations2_multicell_2035.CheckP22035.test_record) ... ok
137 | 2026-11-15T10:37:15.0571852Z test_same_source_replay (test_p2_postulations2_multicell_2035.CheckP22035.test_same_source_replay) ... FAIL
138 | 2026-11-15T10:37:15.0584639Z 
139 | 2026-11-15T10:37:15.0585128Z ======================================================================
140 | 2026-11-15T10:37:15.0587429Z FAIL: test_same_source_replay (test_p2_postulations2_multicell_2035.CheckP22035.test_same_source_replay)
141 | 2026-11-15T10:37:15.0589826Z ----------------------------------------------------------------------
142 | 2026-11-15T10:37:15.0591327Z Traceback (most recent call last):
143 | 2026-11-15T10:37:15.0594816Z   File "/home/runner/work/postulations-dynamic-door/postulations-dynamic-door/tests/test_p2_postulations2_multicell_2035.py", line 38, in test_same_source_replay
144 | 2026-11-15T10:37:15.0598222Z     self.assertEqual(p.stdout,original("result.json"))
145 | 2026-11-15T10:37:15.0599750Z     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
146 | 2026-11-15T10:37:15.0603721Z AssertionError: b'{\n[1892 chars] "3.14.4"\n  },\n  "families": {\n    "A1-only[8037 chars]n}\n' != b'{\n[1892 chars] "3.13.5"\n  },\n  "families": {\n    "A1-only[8037 chars]n}\n'
147 | 2026-11-15T10:37:15.0606890Z 
148 | 2026-11-15T10:37:15.0607602Z ----------------------------------------------------------------------
149 | 2026-11-15T10:37:15.0609197Z Ran 9 tests in 0.300s
150 | 2026-11-15T10:37:15.0609844Z 
151 | 2026-11-15T10:37:15.0610291Z FAILED (failures=1)
152 | 2026-11-15T10:37:15.0624326Z ##[error]Process completed with exit code 1.
```

## Later passing replay

GitHub original run ID: `43705053421`; job ID: `132784233188`. Source URL (may be private): https://github.com/CodeDiggs/postulations-dynamic-door/actions/runs/43705053421

Original job-log lines 135–142, line numbers added; terminal ANSI colors removed:

```text
135 | 2026-11-15T10:38:30.1267002Z test_archived_hashes (test_p2_postulations2_multicell_2035.CheckP22035.test_archived_hashes) ... ok
136 | 2026-11-15T10:38:30.1270255Z test_record (test_p2_postulations2_multicell_2035.CheckP22035.test_record) ... ok
137 | 2026-11-15T10:38:30.3154823Z test_same_source_replay (test_p2_postulations2_multicell_2035.CheckP22035.test_same_source_replay) ... ok
138 | 2026-11-15T10:38:30.3158507Z 
139 | 2026-11-15T10:38:30.3160032Z ----------------------------------------------------------------------
140 | 2026-11-15T10:38:30.3163214Z Ran 9 tests in 0.384s
141 | 2026-11-15T10:38:30.3164423Z 
142 | 2026-11-15T10:38:30.3165068Z OK
```

## Interpretation and limitations

The first selected job records one failing test out of nine, with a bytewise replay mismatch that includes Python provenance versions `3.14.4` versus `3.13.5`. The later selected job records nine tests passing. This establishes that an Actions test outcome changed in a tightly selected case; it is **not** independent verification of mathematical validity, scientific hypothesis testing, or scientific claim adoption. The associated PR and source patch are not included here. An independent reviewer should examine the full original logs and patch under controlled access if claiming the exact cause, not infer causality solely from this excerpt.

**Redaction/selection:** All job lines outside the stated inclusive line ranges are omitted; escape formatting removed. No private run artifacts or credentials intentionally included. Original log authenticity is source-side and not guaranteed by the copied excerpt alone.
