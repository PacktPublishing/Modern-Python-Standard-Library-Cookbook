import pathlib

print(list(pathlib.Path('.').glob('*.py')))

print(list(pathlib.Path('.').glob('**/*.py')))