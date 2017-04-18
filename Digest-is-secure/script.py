#!/usr/bin/env python
# coding:utf-8

# import md5
import requests
import hashlib

pass_hash = "c627e19450db746b739f41b64097d449"

f = open("brute_list_num_1_8", "r")


def main():
    for line in f:
        target = "q9:secret:"+line.rstrip()
        line_md5 = hashlib.md5(target).hexdigest()
        # print line.rstrip() + ": " + line_md5
        print target
        # if line_md5 is hashだとダメ
        if line_md5 == pass_hash:
            print "\nFOUND!!\n\npassword: "+line
            return

if __name__ == "__main__":
    main()
    f.close()
