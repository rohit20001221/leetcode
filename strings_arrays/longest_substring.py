def longestSubString(s):
    m = {}

    l = 0
    r = 0
    maxlength = 0

    while(l < len(s) and r < len(s)):
        el = s[r]
        if(el in m):
            l = max(l, m[el]+1)
        
        m[el] = r
        maxlength = max(maxlength, r-l+1)
        r += 1
    
    return maxlength

print(longestSubString('abaacad'))