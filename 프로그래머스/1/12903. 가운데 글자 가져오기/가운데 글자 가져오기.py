def solution(s):
    i=int(len(s)/2)
    if len(s)%2==1:
        return s[i]
    else:
        return s[i-1:i+1]