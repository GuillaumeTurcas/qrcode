import qrcode
from PIL import Image


def create_qrcode():
    data = input("Put data here : ")
    img_name = input("Name your image : ")

    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(img_name)


def create_qrcode_logo():

    # taking base width
    basewidth = 100

    logo = Image.open(input("Logo : "))

    # adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))

    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    data = input("Put data here : ")
    img_name = input("Name your image : ")

    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image().convert('RGB')

    pos = ((img.size[0] - logo.size[0]) // 2,
           (img.size[1] - logo.size[1]) // 2)

    img.paste(logo, pos)
    img.save(img_name)


if __name__ == "__main__":
    create_qrcode() \
        if input("Do you want a logo on your QRCode ? (y/n) ") == "n"\
        else create_qrcode_logo()
