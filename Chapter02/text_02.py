s = 'Today the weather is nice'
s2 = 'Today the weater is nice'
s3 = 'Yesterday the weather was nice'
s4 = 'Today my dog ate steak'

import difflib
print(difflib.SequenceMatcher(None, s, s2, False).ratio())
print(difflib.SequenceMatcher(None, s, s3, False).ratio())
print(difflib.SequenceMatcher(None, s, s4, False).ratio())
