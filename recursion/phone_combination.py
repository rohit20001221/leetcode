def phoneCombination(s):
    ans = []
    backTracking(s, ans, 0, '')
    return ans

m = {
    '2':'ABC',
    '3':'DEF',
    '4':'GHI',
    '5':'JKL',
    '6':'MNO',
    '7':'PQRS',
    '8':'TUV',
    '9':'WXYZ'
}

def backTracking(s, ans, index, current):
    if index > len(s):
        return
    
    if len(current) == len(s):
        ans.append(current)
        return
    
    currentDigit = s[index]
    # print(currentDigit)
    currentString = m[currentDigit]
    # print(currentString)

    for i in range(len(currentString)):
        backTracking(s, ans, index+1, current + currentString[i])

print(phoneCombination('243'))