from cipher.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text, key):
        text = text.upper()
        result = ""

        for char in text:
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx + key) % len(self.alphabet)
                result += self.alphabet[new_idx]
            else:
                result += char

        return result

    def decrypt_text(self, text, key):
        text = text.upper()
        result = ""

        for char in text:
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx - key) % len(self.alphabet)
                result += self.alphabet[new_idx]
            else:
                result += char

        return result
