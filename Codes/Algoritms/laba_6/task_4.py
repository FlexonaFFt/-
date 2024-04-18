n = int(input())
points = list(map(int, input().split()))
total_points = sum(points)

dp = [False] * (total_points + 1)
dp[0] = True

for p in points:
    for i in range(total_points, -1, -1):
        if dp[i]:
            dp[i + p] = True

if total_points % 2 == 0 and dp[total_points // 2]:
    print(True)
else:
    print(False)