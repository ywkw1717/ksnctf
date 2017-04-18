#!/usr/bin/env python
# coding:utf-8

# import md5
import hashlib

# hash = "c627e19450db746b739f41b64097d449"
# hash = "6ba48f62389c5972b711c9f6cac66923"

nonce = "bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b"
realm = "secret"
username = "q9"
method_of_http = "GET"
uri_of_contents = "/~q9/"
nc = "00000001"
cnonce = "9691c249745d94fc"
qop = "auth"
# A1 = username + ":" + realm + ":" + password
A1 = "c627e19450db746b739f41b64097d449"
A2 = method_of_http + ":" + uri_of_contents
# h_A1 = hashlib.md5(A1).hexdigest()
h_A2 = hashlib.md5(A2).hexdigest()

response = hashlib.md5(A1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + h_A2).hexdigest()

print "A1: " + A1
# print "h_A1: " + h_A1
print "A2: " + A2
print "h_A2: " + h_A2
print response

if response == "c3077454ecf09ecef1d6c1201038cfaf":
    print "\n\ncorrect!"

# f = open("brute_list_num_1_8", "r")
#
#
# def main():
#     for line in f:
#         # target = "q9:secret:"+line.rstrip()
#         target = "q9:secret:"+line
#         line_md5 = hashlib.md5(target).hexdigest()
#         # print line.rstrip() + ": " + line_md5
#         print target
#         # if line_md5 is hashだとダメ
#         if line_md5 == hash:
#             print "\nFOUND!!\n\npassword: "+line
#             return
#
# if __name__ == "__main__":
#     main()
#     f.close()
