a, b = map(int, input().split())
n = int(input())
c = b + n
a += c//60
c = c%60
if a>=24:
    a = a%24
print(a, c)