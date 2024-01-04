def solution(picture, k):
    answer = []
    for i in picture:
        j=''
        for p in i:
            j+=p*k
        for n in range(k):
            answer.append(j)
    return answer