# metaclass_class_interaction
The main magic methods acting in class and instance creation with a metaclass

Mainly to remind me of how this all works together.

If you run the code you get something like this:
```
META __new__ : <class '__main__.Metacls'> with:(<class '__main__.Metacls'>, 'Base', (), {'__module__': '__main__', '__qualname__': 'Base', '__new__': <classmethod object at 0x101759b00>, '__init__': <function Base.__init__ at 0x101694400>, '__call__': <function Base.__call__ at 0x101694488>, '__classcell__': <cell at 0x101665d38: empty>}) - {}
META __init__ : <class '__main__.Base'> with:('Base', (), {'__module__': '__main__', '__qualname__': 'Base', '__new__': <classmethod object at 0x101759b00>, '__init__': <function Base.__init__ at 0x101694400>, '__call__': <function Base.__call__ at 0x101694488>, '__classcell__': <cell at 0x101665d38: Metacls object at 0x7fc4d8f00a18>}) - {}
META __call__ : <class '__main__.Base'> with: ('Create instance',) - {'key': 'word'}
CLASS __new__ : <class '__main__.Base'> with: (<class '__main__.Base'>,) - {}
CLASS __init__ : <__main__.Base object at 0x101759cc0> with: () - {}
CLASS __call__ : <__main__.Base object at 0x101759cc0> with: ('Call instance',) - {'word': 'key'}
```

Python >= 3.6 requried for the f-strings

For an impressive show with metaclasses and Python 3.6 watch this:
David Beazley - "The Fun of Reinvention":
https://www.youtube.com/watch?v=js_0wjzuMfc
