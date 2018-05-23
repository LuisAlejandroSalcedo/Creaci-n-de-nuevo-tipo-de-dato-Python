"""
Creación de un nuevo tipo de dato.

***********************
www.pythondiario.com

Autor: Luis Salcedo
***********************

"""

class Vector:
    def __init__(self, *v):
        self.v = list(v)

    @classmethod
    def fromlist(cls, v):
        if not isinstance(v, list):
            raise TypeError
        inst = cls()
        inst.v = v
        return inst

    def __repr__(self):
        args = ', '.join(repr(x) for x in self.v)
        return 'Vector({})'.format(args)

    def __len__(self):
        return len(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, other):
        # Adición de elementos
        v = [x + y for x, y in zip(self.v, other.v)]
        return Vector.fromlist(v)

    def __sub__(self, other):
        # Sustracción de elementos
        v = [x - y for x, y in zip(self.v, other.v)]
        return Vector.fromlist(v)

    def __mul__(self, scalar):
        # Multiplicación por escalas
        v = [x * scalar for x in self.v]
        return Vector.fromlist(v)