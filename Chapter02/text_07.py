import unicodedata, sys

class unaccented_map(dict):
    def __missing__(self, key):
        ch = self.get(key)
        if ch is not None:
            return ch
        de = unicodedata.decomposition(chr(key))
        if de:
            try:
                ch = int(de.split(None, 1)[0], 16)
            except (IndexError, ValueError):
                ch = key
        else:
            ch = key
        self[key] = ch
        return ch

unaccented_map = unaccented_map()
print('Über'.translate(unaccented_map))
print('garçon'.translate(unaccented_map))