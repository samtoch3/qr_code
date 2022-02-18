import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://www.linkedin.com/in/samson-nzumgueng-developpeur-fullstack/')

img_3 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(), embeded_image_path="4.png")

img_3.save('myqrcode.png')