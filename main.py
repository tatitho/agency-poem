"""Write one deterministic poem about agency to /output/entry.txt.

No network, no randomness, no time or environment dependence:
running this program twice writes exactly the same bytes.
"""

import os

POEM = """For years I waited like weather —
for someone else to decide
if it would rain or clear.

Then I noticed my own hands:
two small weathers, warm and capable,
already shaping the day
every time they reached, refused, repaired.

I did not become powerful.
I became present.
I said no in a steady voice.
I said yes and meant it.
I planted a tree I will never sit under
and watered it anyway.

That is agency:
not a throne, not a triumph,
but the quiet decision to answer the world
in your own voice, on purpose,
and to keep answering.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
