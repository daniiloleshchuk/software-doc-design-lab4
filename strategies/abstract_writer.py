from abc import ABC


class AbstractWriter(ABC):

    @classmethod
    def write(cls, text):
        raise NotImplementedError
