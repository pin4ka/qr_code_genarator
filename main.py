import qrcode

# from PIL import Image

# image = qrcode.make("6296386131@paytm")
# image.save("myqr.png")
# print(type(image))

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("github.com/pin4ka")  # Enter url for QR
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save("new.png")
