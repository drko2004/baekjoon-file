a = int(input())
b = int(input())
w=0
for i in range(b):
    p, g = map(int, input().split())
    t = p * g
    w += t 
   
if a == w:
    print("Yes")
else:
    print("No")