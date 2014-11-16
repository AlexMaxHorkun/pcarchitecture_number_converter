__author__ = 'Alexander Gorkun'
__email__ = 'mindkilleralexs@gmail.com'

from alexander_gorkun.gui import agnumberconverter as __agnumberconverter
from alexander_gorkun.number_converter import converter as __converter

__conv = __converter.ConverterManager()
__bd_conv = __converter.BinaryDecimalConverter()
__conv.converters.append(__bd_conv)
__hd_conv = __converter.HexadecimalDecimalConverter()
__conv.converters.append(__hd_conv)
__hb_conv = __converter.BinaryHexadecimalConverter(__bd_conv, __hd_conv)
__conv.converters.append(__hb_conv)
application = __agnumberconverter.AGNumberConverterGui(__conv)