import qrcode

url="https://kshitijasharma.github.io/qrcode/"

#generate the qrcode
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

#create the image of the qrcode
img=qr.make_image(fill_color="black", back_color="white")
img=img.resize((300,300))
img.save("D:/fun/qrcode_folder/qrcode.png")

print("QR code generated successfully")