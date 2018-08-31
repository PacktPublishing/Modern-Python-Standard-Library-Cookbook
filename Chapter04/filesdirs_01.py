import os


def traverse(path):
    for basepath, directories, files in os.walk(path):
        for f in files:
            yield os.path.join(basepath, f)

for f in traverse('.'):
    print(f)