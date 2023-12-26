def solution(myString):
    answer = []
    for i in myString:
        if i>'l':
            answer.append(i)
        else:
            answer.append('l')
    return ''.join(answer)