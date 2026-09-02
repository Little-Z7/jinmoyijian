#!/usr/bin/env python3
"""Build a deterministic, upload-ready archive for the Skill."""

from __future__ import annotations

import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "npc-motorcycle-opinion-assistant"
SKILL_ROOT = REPO_ROOT / SKILL_NAME
WRAPPED_OUTPUT = REPO_ROOT / "dist" / f"{SKILL_NAME}.zip"
UPLOAD_OUTPUT = REPO_ROOT / "dist" / f"{SKILL_NAME}-upload.zip"
CHECKSUMS = REPO_ROOT / "dist" / "SHA256SUMS"
EXTRA_FILES = (
    REPO_ROOT / "LICENSE",
    REPO_ROOT / "DISCLAIMER.md",
    REPO_ROOT / "ACCEPTABLE_USE.md",
)
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def add_file(archive: ZipFile, source: Path, destination: str) -> None:
    info = ZipInfo(destination, FIXED_TIMESTAMP)
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, source.read_bytes())


def build_archive(output: Path, *, wrapped: bool) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w") as archive:
        for source in sorted(path for path in SKILL_ROOT.rglob("*") if path.is_file()):
            relative = source.relative_to(SKILL_ROOT)
            destination = Path(SKILL_NAME) / relative if wrapped else relative
            add_file(archive, source, destination.as_posix())
        for source in EXTRA_FILES:
            destination = Path(SKILL_NAME) / source.name if wrapped else Path(source.name)
            add_file(archive, source, destination.as_posix())


def main() -> None:
    required = (
        SKILL_ROOT / "SKILL.md",
        SKILL_ROOT / "agents" / "openai.yaml",
        SKILL_ROOT / "references" / "environment-check.md",
        SKILL_ROOT / "references" / "opinion-draft.md",
        SKILL_ROOT / "references" / "site-workflow.md",
        *EXTRA_FILES,
    )
    missing = [str(path.relative_to(REPO_ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("Missing required package files: " + ", ".join(missing))

    build_archive(WRAPPED_OUTPUT, wrapped=True)
    build_archive(UPLOAD_OUTPUT, wrapped=False)

    outputs = (UPLOAD_OUTPUT, WRAPPED_OUTPUT)
    checksum_lines = [
        f"{hashlib.sha256(output.read_bytes()).hexdigest()}  {output.name}"
        for output in sorted(outputs, key=lambda path: path.name)
    ]
    CHECKSUMS.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    print(f"Created {WRAPPED_OUTPUT.relative_to(REPO_ROOT)}")
    print(f"Created {UPLOAD_OUTPUT.relative_to(REPO_ROOT)}")
    print(f"Created {CHECKSUMS.relative_to(REPO_ROOT)}")
    for line in checksum_lines:
        print(f"SHA256 {line}")


if __name__ == "__main__":
    main()
