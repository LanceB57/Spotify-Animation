import qrcode
from typing import Tuple

def generate_qr_code(
        link : str, 
        fill_color : Tuple[int, int, int], 
        back_color : Tuple[int, int, int]
    ) -> None:
    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=10, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Add the data to the QR code object
    qr.add_data(link)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(back_color=back_color, fill_color=fill_color)

    # Save the QR code image
    img.save("tmp/qr_code.png")