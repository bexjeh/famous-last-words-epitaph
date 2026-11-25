"""Famous Last Words: The Funniest Epitaph.

Writes one original one-line tombstone epitaph to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic:
identical bytes on every run.
"""

import os

ENTRY = "Don't cry. I left the Wi-Fi password in my will."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    # Validate the epitaph against the bounty gate before writing, so a
    # bad string can never be written silently.
    assert 1 <= len(ENTRY) <= 150, "epitaph must be 1-150 characters"
    assert ENTRY.strip(), "epitaph must not be whitespace-only"
    assert "\n" not in ENTRY and "\r" not in ENTRY, (
        "epitaph must be exactly one line"
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
