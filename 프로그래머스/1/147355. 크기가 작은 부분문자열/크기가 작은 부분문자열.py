def solution(t, p):
    answer=0
    T=len(t)
    P=len(p)
    for i in range(T-P+1):
        a=t[i:i+P]
        if int(a)<=int(p):
            answer+=1
    return answer