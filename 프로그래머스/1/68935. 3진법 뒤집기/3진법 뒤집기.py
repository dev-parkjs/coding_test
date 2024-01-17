def solution(n):
    answer = ''
    while n>0:
        n,t=divmod(n,3)
        answer+=str(t)
    return int(answer,3)
