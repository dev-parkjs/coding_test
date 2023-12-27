from datetime import datetime
def solution(date1, date2):
    answer = 0

    date1 = datetime(date1[0], date1[1], date1[2])
    date2 = datetime(date2[0], date2[1], date2[2])
    
    if date1 < date2:
        return 1
    else: 
        return 0
    return answer