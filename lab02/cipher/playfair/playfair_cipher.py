class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace('J', 'I')
        seen = set()
        matrix = []

        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for char in alphabet:
            if char not in seen:
                matrix.append(char)

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_position(self, matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j

    def preprocess_text(self, text):
        text = text.upper().replace('J', 'I')
        result = ""
        i = 0

        while i < len(text):
            a = text[i]
            b = ''

            if i + 1 < len(text):
                b = text[i+1]
                if a == b:
                    result += a + 'X'
                    i += 1
                else:
                    result += a + b
                    i += 2
            else:
                result += a + 'X'
                i += 1

        return result

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.preprocess_text(plain_text)
        encrypted = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i+1]
            r1, c1 = self.find_position(matrix, a)
            r2, c2 = self.find_position(matrix, b)

            if r1 == r2:
                encrypted += matrix[r1][(c1+1)%5]
                encrypted += matrix[r2][(c2+1)%5]

            elif c1 == c2:
                encrypted += matrix[(r1+1)%5][c1]
                encrypted += matrix[(r2+1)%5][c2]

            else:
                encrypted += matrix[r1][c2]
                encrypted += matrix[r2][c1]

        return encrypted

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            r1, c1 = self.find_position(matrix, a)
            r2, c2 = self.find_position(matrix, b)

            if r1 == r2:
                decrypted += matrix[r1][(c1-1)%5]
                decrypted += matrix[r2][(c2-1)%5]

            elif c1 == c2:
                decrypted += matrix[(r1-1)%5][c1]
                decrypted += matrix[(r2-1)%5][c2]

            else:
                decrypted += matrix[r1][c2]
                decrypted += matrix[r2][c1]

        return decrypted
