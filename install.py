#!/usr/bin/env python2

import os
import shutil
import stat
import sys

try:
    import config
except ImportError:
    print 'Created personal config.py for your customizations'
    shutil.copyfile('config.py.dist', 'config.py')
    import config

TEMPLATE_FILE = 'shline.py.tpl'
OUTPUT_FILE = 'shline.py'
SEGMENTS_DIR = 'segments'
THEMES_DIR = 'themes'


def load_source(srcfile):
    try:
        with open(srcfile) as f:
            return f.read() + '\n\n'
    except IOError:
        print 'Could not open', srcfile
        return ''


if __name__ == "__main__":
    source = load_source(TEMPLATE_FILE)
    source += load_source(os.path.join(THEMES_DIR, 'default.py'))
    source += load_source(os.path.join(THEMES_DIR, config.THEME + '.py'))
    for segment in config.SEGMENTS:
        source += load_source(os.path.join(SEGMENTS_DIR, segment + '.py'))
    source += 'sys.stdout.write(shline.draw())\n'

    try:
        with open(OUTPUT_FILE, 'w') as f:
            f.write(source)
            st = os.fstat(f.fileno())
            os.fchmod(f.fileno(), st.st_mode | stat.S_IEXEC)
        print OUTPUT_FILE, 'saved successfully'
    except IOError:
        print 'ERROR: Could not write to shline.py. Make sure it is writable'
        sys.exit(1)

