from __future__ import annotations

import argparse
import os.path
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Checks for existing symlinks.')
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        if os.path.islink(filename):
            print(f'{filename}: Existing symlink')
            retv = 1

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
