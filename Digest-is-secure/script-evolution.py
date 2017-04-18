#!/usr/bin/env python
# coding:utf-8

# import md5
import hashlib

# hash = "c627e19450db746b739f41b64097d449"
# hash = "6ba48f62389c5972b711c9f6cac66923"

password = "c627e19450db746b739f41b64097d449"
nonce = "bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b"
realm = "secret"
username = "q9"
method_of_http = "GET"
uri_of_contents = "/~q9/"
nc = "00000002"
cnonce = "6945eb2a7ba8cf7f"
qop = "auth"
A2 = method_of_http + ":" + uri_of_contents
h_A2 = hashlib.md5(A2).hexdigest()

f = open("brute_list_upper_lower_num", "r")


def main():
    for line in f:
        A1 = username + ":" + realm + ":" + line.rstrip()
        print A1
        h_A1 = hashlib.md5(A1).hexdigest()

        response = hashlib.md5(h_A1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + h_A2).hexdigest()
        # target = "q9:secret:"+line.rstrip()
        # target = "q9:secret:"+line
        # line_md5 = hashlib.md5(target).hexdigest()
        # print line.rstrip() + ": " + line_md5
        # print target
        # if line_md5 is hashだとダメ
        # if line_md5 == hash:
        if response == "d9f18946e5587401c303b34e00a059eb":
            print "\nFOUND!!\n\npassword: "+line
            return

if __name__ == "__main__":
    main()
    f.close()
