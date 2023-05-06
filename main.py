import qrcode

# define the data to be encoded in the QR code
data = "https://github.com/DC-21?tab=repositories"

# create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
qr.add_data(data)

# compile the QR code
qr.make(fit=True)

# generate an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# save the image
img.save("qrcode.png")
