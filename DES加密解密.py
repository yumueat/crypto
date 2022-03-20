from Crypto.Cipher import DES
import binascii
def main():
    key = b'abcdefgh'
    des = DES.new(key,DES.MODE_ECB)
    text = "hello world"
    text = text + (8-len(text)%8)*"="
    # print(text)
    encrypt_text = des.encrypt(text.encode())
    # print(encrypt_text)
    encrypt_res = binascii.b2a_hex(encrypt_text)

    decrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_res = des.decrypt(decrypt_text)
    decrypt_res = decrypt_res.decode()
    # decrypt_res = decrypt_res.rstrip("=")
    print(decrypt_res)
    print(encrypt_res)
if __name__ == '__main__':
    main()