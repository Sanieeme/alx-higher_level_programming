#!/usr/bin/python3
for l in range(97, 123):
    if l in [101, 113]:
        continue
    print("{}". format(chr(l)), end="")
