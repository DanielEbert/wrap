#!/usr/bin/env python3

import sys
import os

HFUZZ_CXX = "/home/user/Downloads/honggfuzz/hfuzz_cc/hfuzz-g++"
HFUZZ_CC = "/home/user/Downloads/honggfuzz/hfuzz_cc/hfuzz-gcc"


def main() -> int:
    print(sys.argv)

    argv0_real = f'{sys.argv[0]}_real'
    if os.path.isfile(argv0_real):
        # Honggfuzz will know whether to call CXX or CC
        os.environ['HFUZZ_CXX_PATH'] = argv0_real
        os.environ['HFUZZ_CC_PATH'] = argv0_real

    is_cxx = '++' in os.path.basename(sys.argv[0])
    if is_cxx:
        os.execvp(HFUZZ_CXX, ['c++'] + sys.argv[1:])
    else:
        os.execvp(HFUZZ_CC, ['cc'] + sys.argv[1:])


if __name__ == '__main__':
    raise SystemExit(main())
