def solution(numbers):
    answer = 0
    ㅅㅂ_왜_이렇게_바꿔야함 = []
    for i in numbers:
        ㅅㅂ_왜_이렇게_바꿔야함.append(i)
    ㅅㅂ_왜_이렇게_바꿔야함.sort()
    answer = ㅅㅂ_왜_이렇게_바꿔야함[-1]*ㅅㅂ_왜_이렇게_바꿔야함[-2]
    return answer