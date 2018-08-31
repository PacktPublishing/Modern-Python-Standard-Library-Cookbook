# Write a file with latin-1 encoding
with open('/tmp/somefile.txt', mode='w', encoding='latin-1') as f:
    f.write('This is some latin1 text: "è già ora"')

# Read back file with latin-1 encoding.
with open('/tmp/somefile.txt', encoding='latin-1') as f:
    txt = f.read()
    print(txt)