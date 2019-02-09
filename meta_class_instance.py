class Metacls(type):

    @classmethod
    def __new__(mcs, *args, **kwargs):
        # make a new class object from mcs
        print(f"META __new__ : {mcs} with:{args} - {kwargs}")
        # returns a class
        return super().__new__(*args, **kwargs)

    def __init__(cls, *args, **kwargs):
        # initialize the cls
        print(f"META __init__ : {cls} with:{args} - {kwargs}")
        # returns None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # make an instance of a cls - a call on the class
        print(f"META __call__ : {cls} with: {args} - {kwargs}")
        # returns an instance of cls
        return super().__call__(*args, **kwargs)


class Base(metaclass=Metacls):

    @classmethod
    def __new__(cls, *args, **kwargs):
        # make a new instance object of cls
        print(f"CLASS __new__ : {cls} with: {args} - {kwargs}")

        # returns an instance of cls
        return super().__new__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        # initialize the instance self
        print(f"CLASS __init__ : {self} with: {args} - {kwargs}")

        # returns None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        # a call on the instance
        print(f"CLASS __call__ : {self} with: {args} - {kwargs}")

        # can return anything or None
        return


instance = Base()
value = instance()
