def solution(arr, k):
    answer=[]
    if k%2==0:
        for i in arr:
            new=i+k
            answer.append(new)
    else:
        for i in arr:
            new=i*k
            answer.append(new)
    return answer