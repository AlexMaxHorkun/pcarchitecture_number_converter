__author__ = 'Alexander Gorkun'
__email__ = 'mindkilleralexs@gmail.com'

from alexander_gorkun.gui import agnumberconverter
from alexander_gorkun.number_converter import converter

conv=converter.ConverterManager()
bdConv=converter.BinaryDecimalConverter()
conv.converters.append(bdConv)
hdConv=converter.HexadecimalDecimalConverter()
conv.converters.append(hdConv)
hbConv=converter.BinaryHexadecimalConverter(bdConv, hdConv)
conv.converters.append(hbConv)
app=agnumberconverter.AGNumberConverterGui(conv)
app.start()