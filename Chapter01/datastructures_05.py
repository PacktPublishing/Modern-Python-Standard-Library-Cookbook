from collections import defaultdict

rd = defaultdict(list)
for name, num in [('ichi', 1), ('one', 1), ('uno', 1), ('un', 1)]:
  rd[num].append(name)

print(rd)
