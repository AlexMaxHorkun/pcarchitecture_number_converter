__author__ = 'Alexander Gorkun'
__email__ = 'mindkilleralexs@gmail.com'

NUMERATION_BINARY = 1
NUMERATION_DECIMAL = 2
NUMERATION_HEXADECIMAL = 3


class Converter(object):
    def can_convert(self, fromnum, tonum):
        """
        Checks if converter can convert from one system to another.
        :param tonum: System to convert to.
        :param fromnum: System to convert from.
        :return: If converter can convert from system to system, Bool.
        """
        raise NotImplementedError()

    def convert(self, number, fromsystem, tosystem):
        """
        Converts a number from one numeration system to another.
        :param number: Integer.
        :param fromsystem: Number's numeration system.
        :param tosystem: Result's numeration system.
        :return: Integer.
        """
        raise NotImplementedError()


class ConverterManager(Converter):
    converters=[]

    def can_convert(self, fromnum, tonum):
        if fromnum==tonum:
            return True
        for c in self.converters:
            if c.can_convert(fromnum, tonum):
                return True
        return False

    def convert(self, number, fromsystem, tosystem):
        if fromsystem==tosystem:
            return number
        for c in self.converters:
            if c.can_convert(fromsystem, tosystem):
                return c.convert(number, fromsystem, tosystem)
        raise ValueError("Cannot convert from system %d to %d" % (fromsystem, tosystem))


class BinaryDecimalConverter(Converter):
    def can_convert(self, fromnum, tonum):
        return (fromnum==NUMERATION_BINARY and tonum==NUMERATION_DECIMAL) \
            or (fromnum==NUMERATION_DECIMAL and tonum==NUMERATION_BINARY)

    def convert(self, number, fromsystem, tosystem):
        if fromsystem==NUMERATION_BINARY:
            converted=0
            for i in range(0, len(number)):
                converted+=int(number[-i-1]) * 2 ** i
            return converted
        elif fromsystem==NUMERATION_DECIMAL:
            converted=""
            n=number
            while True:
                converted=str(int(n) % 2)+converted
                if int(n) <= 2:
                    converted=str(int(int(n) / 2))+converted
                    break
                n=int(n) // 2
            return converted
        else:
            raise RuntimeError()


class HexadecimalDecimalConverter(Converter):
    def can_convert(self, fromnum, tonum):
        return (fromnum==NUMERATION_HEXADECIMAL and tonum==NUMERATION_DECIMAL) \
            or (fromnum==NUMERATION_DECIMAL and tonum==NUMERATION_HEXADECIMAL)

    def convert(self, number, fromsystem, tosystem):
        if fromsystem==NUMERATION_HEXADECIMAL:
            converted=0
            for i in range(0, len(number)):
                n=str(number[-i-1])
                n.upper()
                if n=="F":
                    n=15
                elif n=="E":
                    n=14
                elif n=="D":
                    n=13
                elif n=="C":
                    n=12
                elif n=="B":
                    n=11
                elif n=="A":
                    n=10
                converted+=int(n) * (16 ** i)
            return converted
        elif fromsystem==NUMERATION_DECIMAL:
            converted=""
            n=number
            while True:
                if int(n) <= 15:
                    t=int(n)
                else:
                    t=int(n) % 16
                if t==15:
                    t="F"
                elif t==14:
                    t="E"
                elif t==13:
                    t="D"
                elif t==12:
                    t="C"
                elif t==11:
                    t="B"
                elif t==10:
                    t="A"
                converted=str(t)+converted
                if int(n) <= 15:
                    break
                n=int(n) // 16
            return converted
        else:
            raise RuntimeError()


class BinaryHexadecimalConverter(Converter):
    __binary_decimal = None
    __hex_decimal = None

    def __init__(self, bdConverter, hdConverter):
        """
        Needs two converters - binary-decimal, hex-decimal.
        :param bdConverter: BinaryDecimalConverter
        :param hdConverter: HexadecimalDecimalConverter
        """
        assert bdConverter.can_convert(NUMERATION_BINARY, NUMERATION_DECIMAL)
        assert hdConverter.can_convert(NUMERATION_DECIMAL, NUMERATION_HEXADECIMAL)
        self.__binary_decimal=bdConverter
        self.__hex_decimal=hdConverter

    def can_convert(self, fromnum, tonum):
        return (fromnum==NUMERATION_HEXADECIMAL and tonum==NUMERATION_BINARY) \
            or (fromnum==NUMERATION_BINARY and tonum==NUMERATION_HEXADECIMAL)

    def convert(self, number, fromsystem, tosystem):
        if fromsystem==NUMERATION_BINARY:
            return self.__hex_decimal.convert(
                self.__binary_decimal.convert(number, NUMERATION_BINARY, NUMERATION_DECIMAL),
                NUMERATION_DECIMAL,
                NUMERATION_HEXADECIMAL
            )
        elif fromsystem==NUMERATION_HEXADECIMAL:
            return self.__binary_decimal.convert(
                self.__hex_decimal.convert(number, NUMERATION_HEXADECIMAL, NUMERATION_DECIMAL),
                NUMERATION_DECIMAL,
                NUMERATION_BINARY
            )
        else:
            raise ValueError()