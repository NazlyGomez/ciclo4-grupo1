from abc import ABCMeta

import data as data
import self as self


class ModeloAbstracto(metaclass=ABCMeta):
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
