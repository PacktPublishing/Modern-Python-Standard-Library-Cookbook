import pathlib

path = pathlib.Path('somefile.txt')
path.write_text('Hello World')  # Write some text into file.

print(path.resolve())  # Print absolute path

print(path.read_text())  # Check the file content

path.unlink()  # Destroy the file
try:
    print(path.resolve())  # Print absolute path
except Exception as e:
    print(e)

path = pathlib.Path('.')
path = path.resolve()
print(path)

path = path / '..'
print(path.resolve())
