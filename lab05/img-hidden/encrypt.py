import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # kết thúc

    data_index = 0

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    output_path = "encoded_image.png"
    img.save(output_path)
    print("Đã giấu tin vào:", output_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python encrypt.py <image_path> <message>")
    else:
        image_path = sys.argv[1]
        message = sys.argv[2]
        encode_image(image_path, message)