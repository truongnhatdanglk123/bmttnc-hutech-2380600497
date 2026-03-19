from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# ================= SOCKET =================
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# ================= RSA =================
# tạo key cho client
client_key = RSA.generate(2048)

# nhận public key server
server_public_key = RSA.import_key(client_socket.recv(2048))

# gửi public key client cho server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# nhận AES key (đã mã hóa)
encrypted_aes_key = client_socket.recv(2048)

# giải mã AES key bằng private key client
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# ================= AES =================
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# ================= RECEIVE =================
def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received: {decrypted_message}")
        except:
            break

# ================= THREAD =================
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# ================= SEND =================
while True:
    message = input("Enter message ('exit' to quit): ")
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)

    if message == "exit":
        break

# ================= CLOSE =================
client_socket.close()