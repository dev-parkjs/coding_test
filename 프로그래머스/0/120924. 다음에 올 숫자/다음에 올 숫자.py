def solution(common):
    one,two,three=common[:3]
    if two-one==three-two:
        answer=common[-1]+(three-two)
    elif two//one==three//two:
        answer=common[-1]*(three//two)
    return answer
