import zipfile
import os

def zipdir(archive_name, directory):
    with zipfile.ZipFile(
        archive_name, 'w', compression=zipfile.ZIP_DEFLATED
    ) as archive:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                abspath = os.path.join(root, filename)
                relpath = os.path.relpath(abspath, directory)
                archive.write(abspath, relpath)

zipdir('/tmp/test.zip', '_build/doctrees')
with zipfile.ZipFile('/tmp/test.zip') as archive:
    for n in archive.namelist():
        print(n)











