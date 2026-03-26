import sys
from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for i in range(3):
                binary_message += str(pixel[i] & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))

        if char == '\xFE':  # ký tự kết thúc
            break

        message += char

    return message


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <image_path>")
    else:
        image_path = sys.argv[1]
        message = decode_image(image_path)
        print("Message:", message)