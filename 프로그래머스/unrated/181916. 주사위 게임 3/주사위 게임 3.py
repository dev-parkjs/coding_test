def solution(a, b, c, d):
    answer = 0
    nums=[a,b,c,d]
    counts=[nums.count(i) for i in nums]
    
    if max(counts)==4:
        return a*1111
    elif max(counts)==3:
        i=nums[counts.index(1)]
        j=nums[counts.index(3)]
        return (10*j+i)**2
    elif max(counts)==2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums) 
    