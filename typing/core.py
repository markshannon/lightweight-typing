
from enum import Enum

__all__ = [ "Any", "TypeVar"]

class Type:

    def __init__(self, name:str):
        self.__name__ = name

    def __repr__(self):
        return self.__name__


Any = Type("Any")


class Variance(Enum):
    Covariant = 1
    Invariant = 0
    Contravariant = -1


class TypeVar(Type):

    def __init__(self, name:str, variance:Variance=Variance.Invariant):
        super().__init__("~"+name)
        self.variance = variance

