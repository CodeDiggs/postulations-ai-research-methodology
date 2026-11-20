#!/usr/bin/env python3
"""Verify the local release snapshot using only Python's standard library.

Run from the repository root:
    python3 tools/verify_evidence.py

This verifies the bytes recorded in the manifest and screens a small set of
high-risk patterns. It is NOT a secret scanner, rights audit, source-authentication
service, or evidence that the science is valid.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "evidence" / "PROVENANCE_MANIFEST.json"
SUSPICIOUS = {
    "GitHub personal access token": re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{40,})\b"),
    "Private-key block": re.compile(rb"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    "OSF view-only access parameter": re.compile(rb"(?i)view_only=[0-9a-f]{12,}"),
    "ChatGPT private Library file parameter": re.compile(rb"(?i)chatgpt\.com/library\?file_id="),
    "E-mail address in selected exhibits": re.compile(rb"(?i)\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}\b"),
}


def git_blob_sha1(data: bytes) -> str:
    header = ("blob %d\0" % len(data)).encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = (
        [manifest["manuscript"]]
        + manifest["exact_copies"]
        + manifest["derived_or_excerpted"]
    )
    failures = []
    seen = set()
    for record in records:
        rel = pathlib.PurePosixPath(record["deposited_path"])
        if rel.is_absolute() or ".." in rel.parts or str(rel) in seen:
            failures.append(f"Unsafe or repeated path: {rel}")
            continue
        seen.add(str(rel))
        target = ROOT.joinpath(*rel.parts)
        if not target.is_file():
            failures.append(f"Missing: {rel}")
            continue
        data = target.read_bytes()
        digest = git_blob_sha1(data)
        expected = record["deposited_git_blob_sha1"]
        if digest != expected:
            failures.append(f"Content mismatch: {rel} (Git blob {digest})")
        for issue, regex in SUSPICIOUS.items():
            if regex.search(data):
                failures.append(f"Potentially sensitive ({issue}): {rel}")
        if record.get("kind") == "EXACT_GIT_BLOB_COPY":
            if expected != record.get("source_git_blob_sha1"):
                failures.append(f"Source/copy identity mismatch: {rel}")
    if failures:
        for failure in failures:
            print("FAIL:", failure, file=sys.stderr)
        print(f"{len(failures)} issue(s) require review.", file=sys.stderr)
        return 1
    print(
        f"PASS: {len(records)} staged files match the manifest and pass "
        "the limited pattern checks."
    )
    print(
        "LIMIT: Original private records, provenance claims, permissions, "
        "privacy, historic Git objects and anonymous access were not "
        "independently validated by this script."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(verify())
