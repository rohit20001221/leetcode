def groupAnagram(arr):
    ans = []
    m = {}

    for s in arr:
        key = ''.join(sorted(s))
        m[key] = m.get(key, []) + [s]

    for val in m.values():
        ans.append(val[:])

    return ans

print(groupAnagram(['ab','ba', 'a']))  