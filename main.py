import time
from PIL import Image
import qrcode
import cv2
from pyzbar.pyzbar import decode
import barcode
from barcode.writer import ImageWriter


def generate_simple_qrcode(data):
    imgs = qrcode.make(data)
    imgs.save('qrcode1.png')

    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='red', back_color='white')
    img.save('qrcode2.png')

    print(f'QR Code generate with data = {data}')


def generate_complex_qrcode(data, logo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='blue', back_color='white').convert('RGB')
    logo_display = Image.open(logo)
    logo_display.thumbnail((160, 160))
    logo_pos = ((img.size[0] - logo_display.size[0])//2, (img.size[1] - logo_display.size[1])//2)
    img.paste(logo_display, logo_pos)
    img.save('qrcode.png')

    print(f'QR Code generate with data = {data}')


def read_qrcode_on_image(path_img):
    img = cv2.imread(path_img)
    d = cv2.QRCodeDetector()
    val, points, qr_code = d.detectAndDecode(img)
    print(f'Data of your QR Code = {val}')
    print(decode(img))
    for code in decode(img):
        print(f'Type : {code.type}')
        print('Données du QR Code : ', code.data.decode('utf-8'))


def read_qrcode_on_camera():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # 3 - width
    cap.set(4, 480)  # 4 - height
    used_codes = []
    camera = True
    while camera:
        success, frame = cap.read()
        for code in decode(frame):
            if code.data.decode('utf-8') not in used_codes:
                print('Approved. You can enter')
                print('Données du QR Code : ', code.data.decode('utf-8'))
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(5)
            elif code.data.decode('utf-8') in used_codes:
                print('Sorry, this code has been already used')
                time.sleep(5)
            else:
                pass

            print(f'Type : {code.type}')
            print('Données du QR Code : ', code.data.decode('utf-8'))
        cv2.imshow('Testing-code-scan', frame)
        cv2.waitKey(1)


def generate_barre_code_in_svg(data):
    hr = barcode.get_barcode_class('ean13')
    r = hr(data)
    r.save('code_barre')


def generate_barre_code_in_png(data):
    hr = barcode.get_barcode_class('code39')
    r = hr(data, writer=ImageWriter())
    r.save('code_barre')
