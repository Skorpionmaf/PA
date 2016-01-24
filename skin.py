import types

def become(obj, s_m_add, s_m_del):
    for m in s_m_add:
        setattr(obj, m.__name__, types.MethodType(m, obj))
    for m in s_m_del:
        delattr(obj, m.__name__)

class Skin(type):
    def __new__(meta, clsname, supers, clsdict):
        clsdict['become'] = become
        return type.__new__(meta, clsname, supers, clsdict)

def pop(self):
  top = self.data[-1]
  self.data = self.data[:-1]
  self.top -= 1
  return top

def push(self, v):
  self.data += [v]
  self.top += 1

class stack(metaclass=Skin):
    def __init__(self, dim=10):
        self.dimension = dim
        self.top = 0
        self.data = []
    def is_empty(self): return self.top == 0
    def is_full(self): return self.top == (self.dimension-1)
    def __str__(self):
        return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}". \
                format(self.top, self.dimension, self.data)

