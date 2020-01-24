import pyqrcode
def qr():
    text = input("Enter the Text to Generate QR Code:")
    url = pyqrcode.create(text)
    filename=input("Enter the File Name: ")+".png"
    url.png(filename, scale=8)
    print("--------------------------------------------")
    print("QRcode Generated.")
    print("--------------------------------------------")
qr()
