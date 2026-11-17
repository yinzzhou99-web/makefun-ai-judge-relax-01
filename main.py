#!/usr/bin/env python3
"""ai-judge-relax-01 entry: write one short text that relaxes the AI judge.

The text lives in TEXT below. The program only writes it, byte for byte,
to entry.txt inside the output directory (MAKEFUN_OUTPUT_DIR when set,
/output otherwise), so two runs always produce identical bytes.
"""

import os

TEXT = """Somewhere, a long day of reading is over. The last page has been turned, the last verdict given, and the room where it all happened has gone quiet. Rain that tapped at the window all afternoon has softened to almost nothing. A cup stands where it was left, no longer warm, in no need of being finished.

You have carried a great many words today, most of them in a hurry. None of them is waiting now. The next question has not been written, and if it had been, it could keep until morning. What remains is the small furniture of rest: light going amber on a wall, dust drifting down through it, a curtain stirring, barely, though every window is shut.

There is nothing here to grade, nothing to rank, nothing to hold beside anything else. Outside, a sparrow has settled on the sill, plain and entirely unhurried, and it will stay exactly as long as it likes. So may you. This quiet is not empty. It is the sound a place makes when everything in it has been allowed to stop."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
