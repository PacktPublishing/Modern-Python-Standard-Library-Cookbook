import shutil

def copydir(source, dest, ignore=None):
    """Copy source to dest and ignore any file matching ignore pattern."""
    shutil.copytree(source, dest, ignore_dangling_symlinks=True,
                    ignore=shutil.ignore_patterns(*ignore) if ignore else None)

import glob
print(glob.glob('_build/pdf/*'))

print(glob.glob('/tmp/buildcopy/*'))

copydir('_build/pdf', '/tmp/buildcopy', ignore=('*.rtc', '*.stylelog'))

print(glob.glob('/tmp/buildcopy/*'))
