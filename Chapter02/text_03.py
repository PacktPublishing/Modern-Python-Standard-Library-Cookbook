dictionary = {'ability', 'able', 'about', 'above', 'accept', 'according',
              'account', 'across', 'act', 'action', 'activity', 'actually',
              'add', 'address', 'administration', 'admit', 'adult', 'affect',
              'after', 'again', 'against', 'age', 'agency', 'agent', 'ago',
              'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost',
              'alone', 'along', 'already', 'also', 'although', 'always',
              'American', 'among', 'amount', 'analysis', 'and', 'animal',
              'another', 'answer', 'any', 'anyone', 'anything', 'appear',
              'apply', 'approach', 'area', 'argue', 'arm', 'around', 'arrive',
              'art', 'article', 'artist', 'as', 'ask', 'assume', 'at', 'attack',
              'attention', 'attorney', 'audience', 'author', 'authority',
              'available', 'avoid', 'away', 'baby', 'back', 'bad', 'bag',
              'ball', 'bank', 'bar', 'base', 'be', 'beat', 'beautiful',
              'because', 'become'}
import difflib

def suggest(phrase):
    changes = 0
    words = phrase.split()
    for idx, w in enumerate(words):
        if w not in dictionary:
            changes += 1
            matches = difflib.get_close_matches(w, dictionary)
            if matches:
                words[idx] = matches[0]
    return changes, ' '.join(words)


print(suggest('assume ani answer'))
print(suggest('anoter agrement ahead'))
print(suggest('beautiful art'))
