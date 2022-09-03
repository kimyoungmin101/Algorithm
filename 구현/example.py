def recursive(N, K):
    if K == 0 or N == K:
        return 1
    else:
        return recursive(N-1, K-1) + recursive(N-1, K)

print(recursive(49, 6))