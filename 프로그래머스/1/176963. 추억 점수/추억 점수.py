def solution(name, yearning, photo):
    answer = []
    for i in photo:
        count=0
        for j in i:
            if j in name:
                count+=yearning[name.index(j)]
        answer.append(count)
    return answer