#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        letter = letters
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letters) - 32)
        print("{}".format(letter), end="")
    print()
