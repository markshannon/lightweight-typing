
from .core import Type, TypeVar

__all__ = [ "GenericType", "List", "Dict", "Set", "Tuple" ]


class SpecificType(Type):

    def __init__(self, generic, types):
        if types[-1] == Ellipsis:
            if len(types) == 1:
                typestr = "..."
            else:
                typestr = ", ".join(tp.__name__ for tp in types[:-1]) + ", ..."
        else:
            typestr = ", ".join(tp.__name__ for tp in types)
        super().__init__(generic.__name__ + "[" + typestr + "]")
        self.generic = generic
        self.types = types

class ParameterizableType(Type):

    def __init__(self, name):
        super().__init__(name)
        self.types = {}


    def __getitem__(self, types):
        if not isinstance(types, tuple):
            types = types,
        if types in self.types:
            return self.types[types]
        specific = SpecificType(self, types)
        self.types[types] = specific
        return specific

Tuple = ParameterizableType("Tuple")


class GenericType(ParameterizableType):

    def __init__(self, name, *fields):
        super().__init__(name)
        self.fields = fields

    def __getitem__(self, types):
        if isinstance(types, tuple):
            cnt = len(types)
        else:
            cnt = 1
        if len(self.fields) != cnt:
            raise TypeError("Wrong number of fields")
        return super().__getitem__(types)

T = TypeVar("T")
KT = TypeVar("KT")
VT = TypeVar("VT")

Dict = GenericType("Dict", KT, VT)
List = GenericType("List", T)
Set = GenericType("Set", T)

