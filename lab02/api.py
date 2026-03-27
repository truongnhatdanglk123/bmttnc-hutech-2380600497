from flask import Flask, request, jsonify
from cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair = PlayfairCipher()
transposition = TranspositionCipher()

# Caesar routes
@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted = caesar.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted})


@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted = caesar.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted})

# Vigenere routes
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RailFence routes
@app.route('/api/railfence/encrypt', methods=['POST'])
def rail_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def rail_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Playfair routes
@app.route('/api/playfair/creatematrix', methods=['POST'])
def create_matrix():
    data = request.json
    key = data['key']
    matrix = playfair.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']

    matrix = playfair.create_playfair_matrix(key)
    encrypted = playfair.playfair_encrypt(plain_text, matrix)

    return jsonify({'encrypted_text': encrypted})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']

    matrix = playfair.create_playfair_matrix(key)
    decrypted = playfair.playfair_decrypt(cipher_text, matrix)

    return jsonify({'decrypted_text': decrypted})

# Transposition routes
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted = transposition.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted = transposition.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
