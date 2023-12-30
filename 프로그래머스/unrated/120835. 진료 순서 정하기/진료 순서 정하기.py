def solution(emergency):
    answer = []
    sorted_answer=sorted(emergency,reverse=True)
    for i in emergency:
        index=sorted_answer.index(i)+1
        answer.append(index)
    return answer