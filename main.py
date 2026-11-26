#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Feel Proud: A Family Scene".

Writes one short family scene (one line, 1-280 characters) to
entry.txt in the output directory. The scene: a mother who still cuts
the crusts off her grown child's sandwiches, and the child who quietly
eats those crusts in the car so she never has to know he grew up.
"""

import os

ENTRY = (
    "Mum still cuts the crusts off my sandwiches when I visit, and I'm "
    "forty-one. I eat them in the car so she never has to know I grew up."
)


def validate(text: str) -> str:
    """Return the entry text cleaned, or raise if it breaks the gate.

    The gate accepts UTF-8 text of 1-280 characters that is not only
    white space, and the scene must fit in one or two lines.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if len(cleaned) > 280:
        raise ValueError(f"entry must be at most 280 characters, got {len(cleaned)}")
    if cleaned.count("\n") > 1:
        raise ValueError("entry must fit in one or two lines")
    return cleaned


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
