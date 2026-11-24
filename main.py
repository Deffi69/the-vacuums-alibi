"""make.fun The Vacuum's Alibi entry.

Writes one deadpan excuse from a robot vacuum for missing a spot:
its lidar classified the spot as a permanent resident, and it vacuums
dust -- it does not evict tenants.
"""

import os

LINE = (
    "My lidar classified the spot as a permanent resident. "
    "I vacuum dust; I do not evict tenants."
)


def main() -> None:
    # Guard the competition rules at runtime: one line, 1-200 chars.
    # Fail loudly instead of silently writing an invalid entry.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"entry line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry line must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
