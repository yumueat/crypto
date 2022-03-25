from hashlib import md5
def md5_encrypt(s):
    new_md5 = md5()
    new_md5.update(s.encode())
    return new_md5.hexdigest()

def main():
    print(md5_encrypt("hello world"))

if __name__ == '__main__':
    main()