N = int(input())

P = list(map(int, input().split(' ')))
P.sort()

sums = 0

for i in range(0, N):
    for j in range(0, i+1):
        sums = sums + P[j]

print(sums)