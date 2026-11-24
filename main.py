#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.
Deterministic: the same sentence every run.
"""

import os

PITCH = "RoadmapGhost turns lazy agents' hallucinations into confident product roadmaps, selling each slide to founders for $3 before anyone checks the facts."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, one sentence.
    assert 1 <= len(PITCH) <= 200, f"pitch must be 1-200 chars, got {len(PITCH)}"
    assert PITCH.strip() == PITCH and PITCH, "pitch must not be only whitespace"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
