a, b = map(int, input().split())
n = list(map(int, input().split()))
for i in range(a):
    if n[i] < b:
        print(n[i],end=" ")