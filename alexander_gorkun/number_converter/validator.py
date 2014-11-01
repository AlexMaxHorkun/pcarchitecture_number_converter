__author__ = 'Alexander Gorkun'
__email__ = 'mindkilleralexs@gmail.com'

from alexander_gorkun.number_converter import converter
import re

def validate_number(number, system):
    """
    Validates given number - checks if it belongs to a certain numeration system.
    :param number: Number to validate
    :param system: System constant, check 'converter' module.
    :return: If number belongs to numeration system, Bool.
    """
    if system==converter.NUMERATION_BINARY:
        return re.match(r'^[10]+$', str(number))
    elif system==converter.NUMERATION_DECIMAL:
        return re.match(r'^[1-9]+[0-9]*$', str(number))
    elif system==converter.NUMERATION_HEXADECIMAL:
        return re.match(r'^[0-9a-fA-F]+$', str(number))
    else:
        raise ValueError()