def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer+=str(i)*n
    return answer