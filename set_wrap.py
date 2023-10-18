#!/usr/bin/env python3

import os
import glob
import shutil
import stat

# Regex patterns. '**' does not match hidden directories.
search_paths = [
    'TODO _generated cross compiler'
]

WRAP_PY = './wrap.py'


def main() -> int:
    assert os.path.isfile(WRAP_PY)

    for search_path in search_paths:
        for found_path in glob.glob(search_path, recursive=True):
            found_path_real = found_path + '_real'
            if os.path.isfile(found_path_real):
                print(f'Wrapped already {found_path_real}')
                continue
            shutil.move(found_path, found_path_real)
            shutil.copy(WRAP_PY, found_path)

            os.chmod(found_path, os.stat(found_path).st_mode |
                     stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
