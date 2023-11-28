#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != '0':
        print("{}".format(chr(letter)), end="")
