#!/bin/python

import sys


def print_even_index_char(s):
    l = len(s)
    output = ""
    for i in range(0, l, 2):
        output += s[i]
    return output


def print_odd_index_char(s):
    l = len(s)
    output = ""
    for i in range(1,l,2):
        output += s[i]
    return output


t = int(input())
for a0 in range(0, t):
    s = input()
    print(print_even_index_char(s) + " " + print_odd_index_char(s))

