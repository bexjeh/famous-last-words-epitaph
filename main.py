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
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
