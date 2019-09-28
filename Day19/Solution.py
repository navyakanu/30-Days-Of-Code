from collections import deque


def divisor_sum(num):
    divisor_sum_result = num;
    for i in range(0, num):
        if num % i == 0:
            divisor_sum_result += i;
    return divisor_sum_result;


class Solution:
    pass
