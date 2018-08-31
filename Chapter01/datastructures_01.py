txt = "This is a vast world you can't traverse world in a day"

from collections import Counter
counts = Counter(txt.split())
print(counts)

print(counts.most_common(2))

print(sum(counts.values()))

print(Counter(["hello", "world"]) + Counter(["hello", "you"]))
print(Counter(["hello", "world"]) & Counter(["hello", "you"]))