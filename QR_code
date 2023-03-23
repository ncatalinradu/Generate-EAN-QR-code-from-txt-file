import qrcode

lista_QR = open('coduri_QR.txt','r').readlines()
for cod_QR in lista_QR:
    linie = cod_QR.strip()
    print (linie)
    QR = qrcode.make(linie)
    file_name = 'QR_' + linie + '.jpg'
    QR.save(file_name)
