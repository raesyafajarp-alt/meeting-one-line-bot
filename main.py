#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line entry.

When run, writes a single original sentence to /output/entry.txt: the
one line that could have replaced an entire pointless meeting. It works
because it does the meeting's whole job in one breath -- it states the
shared ground (everyone read it, everyone agrees), makes the decision,
distributes it, and then reclaims the wasted hour. The sting is in the
last clause: the meeting is not just unnecessary, it is the thing that
was going to waste the hour. After this line, there is nothing left to
meet about.
"""

import os

ENTRY = "We've all read the proposal and we all agree, so let's approve it, email the decision to everyone, and give us back the hour this meeting was going to waste."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
