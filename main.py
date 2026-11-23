"""make.fun entry: a plan an AI agent carries out itself to turn $100
into the most money in 30 days.

The plan text is held as a single constant, validated, and written to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).
"""

import os
import sys

# The plan, exactly as audited: 280 characters, every number internally
# consistent (900 plumbers, 30 texts/day x 29 days = 870 texts, 2% of 870
# is 17.4 -> 17 sales, 17 x $999 = $16,983, 17 x $99/mo = $1,683/mo).
PLAN = (
    "Day 1: scrape Google Maps for 900 plumbers in a metro with no website; "
    "build each a free demo site with their name on it. Days 2-30: text 30 "
    "owners/day their demo link; sell it for $999 + $99/mo care. $100: domain, "
    "inbox, SMS. 870 texts at just 2% = 17 sales: $16,983 + $1,683/mo."
)


def validate(plan: str) -> None:
    """Check the plan text meets the competition's entry rules.

    Rules enforced: valid UTF-8, non-blank, 1-280 Unicode code points, and
    a single block of text (no embedded newlines), so the submitted entry
    reads as one plan rather than several fragments.
    """
    if not isinstance(plan, str):
        raise TypeError("plan must be a str")
    plan.encode("utf-8")  # must be valid UTF-8
    if not plan.strip():
        raise ValueError("plan must not be only whitespace")
    if "\n" in plan or "\r" in plan:
        raise ValueError("plan must not contain line breaks")
    n = len(plan)  # Unicode code points
    if not 1 <= n <= 280:
        raise ValueError(f"plan must be 1-280 characters, got {n}")


def main() -> int:
    validate(PLAN)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PLAN)
    print(f"wrote {len(PLAN)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
