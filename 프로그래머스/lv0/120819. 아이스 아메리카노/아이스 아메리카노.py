def solution(money):
    answer = []
    answer.append(money//5500)
    answer.append(money - 5500*answer[0])
    return answer