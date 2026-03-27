from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Trang Caesar
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

# Encrypt
@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    cipher = CaesarCipher()
    encrypted = cipher.encrypt_text(text, key)

    return f"Text: {text}<br>Key: {key}<br>Encrypted: {encrypted}"

# Decrypt
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    cipher = CaesarCipher()
    decrypted = cipher.decrypt_text(text, key)

    return f"Text: {text}<br>Key: {key}<br>Decrypted: {decrypted}"

if __name__ == '__main__':
    app.run(debug=True)
