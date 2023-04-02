from barcode import EAN13
from barcode.writer import ImageWriter

lista_EAN = open('coduri_EAN.txt','r').readlines()
for cod_EAN in lista_EAN:
    linie = cod_EAN.strip()
    print (linie)
    
    EAN = EAN13(linie, writer=ImageWriter())
    file_name = 'EAN_' + linie
    EAN.save(file_name)
