def solution(score):
    answer = []
    result=[]
    for i in score:
        answer.append(sum(i)/len(i))
    arr=sorted(answer,reverse=True)
    for j in answer:
        result.append(arr.index(j)+1)
    return result

