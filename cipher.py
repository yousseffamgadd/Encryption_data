

from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
import os
import time

def encrypt_file_ecb(key, input_file, output_file):
    starttime=time.time()
    with open(input_file, 'rb') as f:
        data = f.read()
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data, DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    runtime=time.time()-starttime
    print("ecb_enc_runtime")
    print(runtime)

def encrypt_file_cbc(key, iv, input_file, output_file):
    starttime2=time.time()
    with open(input_file, 'rb') as f:
        data = f.read()
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_data = pad(data, DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    runtime2=time.time()-starttime2
    print("cbc_enc_runtime")
    print(runtime2)



def decrypt_file_ecb(key, enc_input_ecb, output_file):
    starttime3=time.time()
    with open(enc_input_ecb, 'rb') as f:
        encrypted_data = f.read()
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES.block_size)
    with open(output_file, 'wb') as f:
        f.write(unpadded_data)
    runtime3=time.time()-starttime3
    print("ecb_decrypt_runtime")
    print(runtime3)

def decrypt_file_cbc(key, iv, enc_input_cbc, output_file):
    starttime4=time.time()
    with open(enc_input_cbc, 'rb') as f:
        encrypted_data = f.read()
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES.block_size)
    with open(output_file, 'wb') as f:
        f.write(unpadded_data)
    runtime4=time.time()-starttime4
    print("cbc_decrypt_runtime")
    print(runtime4)

# Example usage
key = b'abcdefgh'  # 8 bytes key
iv = b'12345678'   # 8 bytes IV for CBC mode

input_file = 'text.txt'
output_file_ecb= 'encrypted_ecb.txt'
output_file_cbc= 'encrypted_cbc.txt'
enc_input_ecb = 'encrypted_ecb.txt'
enc_input_cbc = 'encrypted_cbc.txt'
decrypted_output_file_ecb = 'decrypted_ecb.txt'
decrypted_output_file_cbc = 'decrypted_cbc.txt'


if os.path.exists(output_file_ecb):
    decrypt_file_ecb(key, enc_input_ecb, decrypted_output_file_ecb)

if os.path.exists(output_file_cbc):
    decrypt_file_cbc(key, iv, enc_input_cbc, decrypted_output_file_cbc)

if os.path.exists(input_file):
    encrypt_file_cbc(key, iv, input_file, output_file_cbc)
    encrypt_file_ecb(key, input_file, output_file_ecb)

