class Bunch(dict):
   def __getattribute__(self, key):
       try: 
           return self[key]
       except KeyError:
           raise AttributeError(key)
   
   def __setattr__(self, key, value): 
       self[key] = value

b = Bunch(a=5)
print(b.a)
print(b['a'])
