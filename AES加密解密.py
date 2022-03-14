import binascii

from Crypto.Cipher import AES

def main():
    key = "qwertyuiqwertyui".encode()
    text = "hello world"
    text = text + (16-(len(text)%16))*"="
    # print(text)
    aes = AES.new(key,AES.MODE_ECB)
    encrypt_text = aes.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
    decrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_res = aes.decrypt(decrypt_text)
    decrypt_res = decrypt_res.decode()
    # decrypt_res = decrypt_res.rstrip("=")
    print(decrypt_res)
if __name__ == '__main__':
    main()