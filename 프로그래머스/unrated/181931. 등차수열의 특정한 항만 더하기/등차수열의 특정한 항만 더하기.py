def solution(a, d, included):
    answer = 0
    num=0
    for i in range(len(included)):
        answer=a+(d*i)
        if included[i]==1:
            num+=answer
    return num