#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """ defines a functionthat performs minimum number of operation"""
    if n <= 1:
        return 0
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
