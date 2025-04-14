def solution(s1, s2):
    answer = []
    for i in s1:
        if i in s2:
            answer.append(i)
    return len(answer)