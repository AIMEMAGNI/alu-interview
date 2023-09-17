#!/usr/bin/python3

def minOperations(n):
    # If n is 1, it's impossible to achieve more than 1 H.
    if n == 1:
        return 0
    
    # Initialize a list to keep track of minimum operations for each position.
    dp = [0] + [float('inf')] * n
    
    for i in range(2, n+1):
        for j in range(2, i+1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    
    return dp[n] if dp[n] != float('inf') else 0
