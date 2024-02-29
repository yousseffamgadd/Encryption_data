import os

def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S

def PRGA(S):
    x = 0
    y = 0
    while True:
        x = (x + 1) % 256
        y = (y + S[x]) % 256
        S[x], S[y] = S[y], S[x]  # swap
        K = S[(S[x] + S[y]) % 256]
        yield K

def RC4(key, plaintext):
    S = KSA(key)
    keystream = PRGA(S)
    ciphertext = []
    for byte in plaintext:
        ciphertext_byte = byte ^ next(keystream)
        ciphertext.append(ciphertext_byte)
    return bytes(ciphertext)

def encrypt_image(input_filename, output_filename, key):
    with open(input_filename, 'rb') as f:
        plaintext = f.read()
    encrypted_data = RC4(key, plaintext)
    with open(output_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_image(input_filename, output_filename, key):
    with open(input_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = RC4(key, encrypted_data)
    with open(output_filename, 'wb') as f:
        f.write(decrypted_data)

if __name__ == "__main__":
    key = input("Enter a 16-character key: ")
    key = [ord(char) for char in key]

    input_image = "GUC.jpg.png"
    encrypted_image = "encrypted_image.png"
    decrypted_image = "decrypted_image.png"

    encrypt_image(input_image, encrypted_image, key)
    print("Encryption done successfully.")

if os.path.exists(encrypted_image):
        decrypt_image(encrypted_image, decrypted_image, key)
        print("Decryption done successfully.")
    
