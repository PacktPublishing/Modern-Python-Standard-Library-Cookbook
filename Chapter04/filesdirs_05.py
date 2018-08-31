import tempfile, os

with tempfile.NamedTemporaryFile() as f:
  print(f.name)

with tempfile.NamedTemporaryFile() as f:
  os.system('echo "Hello World" > %s' % f.name)
  f.seek(0)
  print(f.read())


