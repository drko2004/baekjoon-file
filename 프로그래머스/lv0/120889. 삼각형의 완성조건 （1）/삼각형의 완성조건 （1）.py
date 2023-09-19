def solution(sides):
    sides.sort()
    print(sides)
    if sides[0]+sides[1] > sides[2]:
        return 1
    else:
        return 2
    