def longestCommonPrefix(strs):
    if strs == None or len(strs) == 0:
        return ""
    return divide(strs, 0, len(strs)-1)

def divide(strs, l, r):
    if(l == r):
        return strs[l]

    mid = (l + r) // 2
    lcpLeft = divide(strs, l, mid)
    lcpRight = divide(strs, mid+1, r)

    return commonPrefix(lcpLeft, lcpRight)

def commonPrefix(lcpLeft, lcpRight):
    min_length = min(len(lcpLeft), len(lcpRight))
    result = ""

    for i in range(min_length):
        if lcpRight[i] == lcpLeft[i]:
            result += lcpLeft[i]
    
    return result

print(longestCommonPrefix(["leetcode", "leet", "lee", "le"]))