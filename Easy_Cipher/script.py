#!/usr/bin/env python

import sys


def main():
    print 'This is the rot13 program.\nPlease input:',
    target = raw_input()

    print 'Do you move several characters?:',
    num = raw_input()

    num = int(num)
    tmp = []
    rot = []

    for i in range(len(target)):
        tmp.append(target[i])

    for i in tmp:
        if (ord(i) >= 65 and ord(i) <= 90):
            rot.append(chr((ord(i) - ord('A') + num) % 26 + ord('A')))
        elif (ord(i) >= 97 and ord(i) <= 122):
            rot.append(chr((ord(i) - ord('a') + num) % 26 + ord('a')))
        else:
            rot.append(i)

    for i in rot:
        sys.stdout.write(i)

if __name__ == '__main__':
    main()
