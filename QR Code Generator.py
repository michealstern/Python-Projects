import qrcode

# img = qrcode.make("https://github.com/michealstern")
# img.save("GitHub_QR_Code.png")


from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)
qr.add_data("GitHub_QR_Code.png")
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("GitHub.png")


