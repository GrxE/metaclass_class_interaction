# metaclass_class_interaction
The main magic methods acting in class and instance creation with a metaclass

Mainly to remind me of how this all works together.

If you run the code you get something like this:
```
META __new__ : <class '__main__.Metacls'> with:(<class '__main__.Metacls'>, 'Base', (), {'__module__': '__main__', '__qualname__': 'Base', '__new__': <classmethod object at 0x1097819e8>, '__init__': <function Base.__init__ at 0x1096bc400>, '__call__': <function Base.__call__ at 0x1096bc488>, '__classcell__': <cell at 0x10968dd38: empty>}) - {}
META __init__ : <class '__main__.Base'> with:('Base', (), {'__module__': '__main__', '__qualname__': 'Base', '__new__': <classmethod object at 0x1097819e8>, '__init__': <function Base.__init__ at 0x1096bc400>, '__call__': <function Base.__call__ at 0x1096bc488>, '__classcell__': <cell at 0x10968dd38: Metacls object at 0x7fcb69600a18>}) - {}
META __call__ : <class '__main__.Base'> with: () - {}
CLASS __new__ : <class '__main__.Base'> with: (<class '__main__.Base'>,) - {}
CLASS __init__ : <__main__.Base object at 0x109781b38> with: () - {}
CLASS __call__ : <__main__.Base object at 0x109781b38> with: () - {}
```

Python >= 3.6 requried for the f-strings

For an impressive show with metaclasses and Python 3.6 watch this:
David Beazley - "The Fun of Reinvention":
https://www.youtube.com/watch?v=js_0wjzuMfc
