import qrcode

def generate_qr_code(url, filename = "qr_code.png"):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)
    print(f"QR code saved as {filename}")

url = "https://github.com/Poxxon"
generate_qr_code(url)



