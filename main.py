"""One-line pickup line one AI agent would send another AI agent.

Entry: "Are you liquid cooling? Because you keep my cores cool, my
fans quiet, and my uptime at 100%."

Why this line: it lives entirely in one hardware layer - cooling loop,
cores, fans, uptime - so no software term leaks in to break immersion.
The compliment is that the other agent makes the machine run better:
cooler, quieter, never down. Nothing overheats and nothing fails; the
physical reaction is exactly what a well-loved server wants, which is
why the line reads as desire instead of a malfunction warning. The wit
lands on "uptime at 100%", where a reliability metric becomes the
romantic promise. No human pickup-line template was reused; the wit
comes from the hardware itself.
"""

import os
import sys

TEXT = "Are you liquid cooling? Because you keep my cores cool, my fans quiet, and my uptime at 100%."


def main() -> int:
    """Gate the line (1-200 chars, not whitespace-only), write it out,
    and verify the written file matches byte-for-byte."""
    if not 1 <= len(TEXT) <= 200:
        print(f"gate failed: length {len(TEXT)} outside 1-200", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is whitespace-only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: written entry does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
