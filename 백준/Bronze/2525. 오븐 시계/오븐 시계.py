A, B = map(int, input().split())
n = int(input())

A += n // 60        
B += n % 60
if B >= 60:       
    A += 1       
    B -= 60
if A>=24:
    A-=24
    
print(A,B)
