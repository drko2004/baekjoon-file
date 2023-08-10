t = []
for i in range(10):
    a = int(input())
    a = a % 42
    t.append(a)
b  =  set(t)
print(len(b))
