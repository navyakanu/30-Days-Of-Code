#!/bin/python

import sys

arr = list(map(int, input().strip().split(' ')))
ans = ""
for i in range(len(arr)-1, -1, -1):
    ans += str(arr[i]) + " "

print(ans)
