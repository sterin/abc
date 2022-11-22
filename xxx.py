import shutil
import sys
import re

def files():
    for line in sys.stdin.readlines():
        m = re.match(r'clang: note: diagnostic msg: ([/a-zA-Z0-9_.-]+)\s*$', line)
        if m:
            yield m.group(1)

for f in files():
    shutil.copy(f, 'staging/')
