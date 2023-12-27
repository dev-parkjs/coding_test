def solution(arr, flag):
    answer = []
    for i,j in enumerate(flag):
        if j:
            for k in range(0,arr[i]*2):
                answer.append(arr[i])
        else:
            for k in range(0,arr[i]):
                answer.pop()
    return answer