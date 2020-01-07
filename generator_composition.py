#programing needs to be able to wrap functions

# func.__name__


import re

def ilen(it):
   return sum(1 for i in it)


def count(chars, accum, sep=' '):
   return accum + ilen(re.finditer(sep, chars)) 


class Monoid:
   def __init__(self, unit, function):
      self.function = function
      self.name = function.__name__
      self.unit = unit

   def __call__(self,*args):
      return self.function(*args)



class FPComposed:
   def __init__(self, *monoids, fp=None, gen=None):
      self.source = gen

      self.functions = []
      for monoid in monoids:
         if(isinstance(monoid, Monoid)):
            f = monoid.function
            f.value = monoid.unit
            setattr(self, monoid.name, f)
            self.functions.append(f)
         else:
            raise Exception('Only Monoids are supported')

   def __iter__(self):
      return self
   
   def __next__(self):
      value = next(self.source)
      for f in self.functions:
         f.value = f(value,f.value)
      return value
      

       

#with open('file', 'r') as fp:
#   gen = FComposed(count,fp=fp)
