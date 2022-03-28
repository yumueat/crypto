from pexpect import pxssh

def login(server,username,password):
    try:
        s = pxssh.pxssh()
        s.login(server,username,password)
        print("login success")
    except:
        print("there is something wrong or login fail")

def main():
    login("192.168.64.128","root","710523")

if __name__ == '__main__':
    main()