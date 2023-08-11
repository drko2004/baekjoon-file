alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = input()
s = list(a)
s = list(set(s))
s.sort()

for i in alpha[0:26]:
    if i in a:
        print(a.index(i), end=' ')
    else:   
        print(-1, end=' ')
      