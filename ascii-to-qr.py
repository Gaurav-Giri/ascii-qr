from PIL import Image
import qrcode

def image_to_ascii(image_path, width=50):  # Reduce width to decrease output size
    chars = "@%#*+=-:. "
    img = Image.open(image_path)
    
    # Resize the image
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, new_height))
    
    img = img.convert("L")
    
    ascii_str = "".join(chars[pixel // 32] for pixel in img.getdata())
    ascii_image = "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
    
    return ascii_image[:2500]  # Limit to 2500 characters (to fit in QR)




def ascii_to_qr(ascii_text, output_qr_path="ascii_qr.png"):
    """Generates a QR code from ASCII text."""
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(ascii_text)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_qr_path)
    print(f"QR code saved as {output_qr_path}")

if __name__ == "__main__":
    image_path = "img_1.png"  # Change to your image file path
    ascii_output = image_to_ascii(image_path)
    
    print("ASCII Output:\n", ascii_output)  # Print ASCII representation
    ascii_to_qr(ascii_output)  # Convert ASCII to QR code
