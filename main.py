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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
