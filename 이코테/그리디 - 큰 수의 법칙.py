N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
Q = M // (K+1); R = M % (K+1)
large = Q * (K * num[-1] + num[-2]) + R * (num[-1])
print(large)