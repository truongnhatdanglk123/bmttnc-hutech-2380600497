class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        ciphertext = [''] * key

        for col in range(key):
            pointer = col

            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key

        return ''.join(ciphertext)

    def decrypt(self, text, key):
        num_of_columns = key
        num_of_rows = (len(text) + key - 1) // key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)

        plaintext = [''] * num_of_rows
        col = 0
        row = 0

        for symbol in text:
            plaintext[row] += symbol
            row += 1

            if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_columns - num_of_shaded_boxes):
                row = 0
                col += 1

        return ''.join(plaintext)