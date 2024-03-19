def solution(n):
    answer = []
    str_num = str(n)
    for i in range(0,len(str_num)):
        answer.append(int(str_num[i]))
    answer.reverse()
    return answer