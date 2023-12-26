def solution(arr, idx):
    answer = 0
    a=[]
    for i in range(idx,len(arr)):
        if arr[i]==1:
            a.append(i)
    if len(a)==0:
        answer=-1
    else:
        answer=min(a)
    return answer