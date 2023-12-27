def solution(myString, pat):
    myString=myString.replace("A","x").replace("B","A").replace("x","B")
    if pat in myString:
        return 1
    else:
        return 0
