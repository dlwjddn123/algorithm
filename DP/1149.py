N = int(input())
arr = []
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

for i in range(1,N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    print(arr[i])

print(min(arr[N-1]))