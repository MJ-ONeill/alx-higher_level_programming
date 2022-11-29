#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(c - 33)), end="")
