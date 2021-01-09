def minWindow(s, t):
    len1 = len(s)
    len2 = len(t)

    hashPat = {}
    hashStr = {}

    for i in t:
        hashPat[t] = hashPat.get(t, 0) + 1
    
    count = 0
    left = 0
    startIndex = -1
    minLength = float("inf")

    for right in range(len1):
        if hashStr.get(s[right]) is None:
            hashStr[s[right]] = 0
        
        hashStr[s[right]] += 1

        if hashPat.get(s[right]) is None:
            hashPat[s[right]] = 0
        
        if count == len2:
            while hashStr.get(s[left]) > hashPat.get(s[left]) or hashPat.get(s[left]) == 0:
                if hashStr.get(s[left]) > hashPat.get(s[left]):
                    hashStr[s[left]] -= 1
                
                left += 1

        windowLen = right - left + 1
        if(minLength > windowLen):
            minLength = windowLen
            startIndex = left
    
    if(startIndex == -1):
        return ""
    
    return s[startIndex:startIndex+minLength]