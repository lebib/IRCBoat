from functools import wraps


class ModuleMetaclass(type):
    def __init__(cls, name, bases, attrs):
        # we gonna wrap the Module class __init__
        # so we save it before

        orig_init = cls.__init__

        # let's wrap that constructor
        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            # we are inside the constructor, call original
            orig_init(*args, **kwargs)
            # lookup bangz in this class attributes
            for bang_name, bang in attrs.items():
                if not bang_name.startswith('_') and \
                   callable(bang):
                    # register the bang
                    self.boat.register_bang(bang_name, bang)

        # set the new __init__ on the class (replace orig_init)
        cls.__init__ = new_init


class Module(metaclass=ModuleMetaclass):
    def __init__(self, boat):
        self.boat = boat
