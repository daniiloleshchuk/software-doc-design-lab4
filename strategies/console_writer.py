from time import sleep

from .abstract_writer import AbstractWriter


class ConsoleWriter(AbstractWriter):
    @classmethod
    def write(cls, text):
        print(text)
