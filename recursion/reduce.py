def solution(s):
    if len(s) == 1:
        return s
    
    sum_ = 0
    
    for i in s:
        sum_ += int(i)
    
    return solution(str(sum_))

print(solution('123456'))