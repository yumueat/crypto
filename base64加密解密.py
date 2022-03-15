import base64
s1 = "hello world"
s2 = base64.b64encode(s1.encode("utf-8"))
print(s2.decode("utf-8"))
s3 = "aGVsbG8gd29ybGQ="
s4 = base64.b64decode(s3.encode("utf-8"))
print(s4.decode("utf-8"))