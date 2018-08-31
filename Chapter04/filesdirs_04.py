import pathlib

stat = pathlib.Path('conf.py').stat()
print(stat)

print(pathlib.Path('conf.py').exists())
print(pathlib.Path('conf.py').is_dir())
print(pathlib.Path('_build').is_dir())
