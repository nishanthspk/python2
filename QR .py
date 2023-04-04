import qrcode

# input the text string you want to encode
text = "Hello, World!"

# create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add the data to the QR code instance
qr.add_data(text)

# compile the QR code instance
qr.make(fit=True)

# create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# save the image file as a PNG file
img.save("qrcode.png")





