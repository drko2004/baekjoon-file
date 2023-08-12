alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = input()
b = a.lower()
arr = []
for i in b:
    if i in alpha[0:17]:
        i = (alpha.index(i)//3)+3
        arr.append(i)
    elif i in alpha[17:22]:
        i = ((alpha.index(i)-1)//3)+3
        arr.append(i)
    elif i in alpha[22:26]:
        i = 10
        arr.append(i)
        
print(sum(arr))