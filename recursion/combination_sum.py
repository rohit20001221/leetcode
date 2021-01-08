def combinationSum(candidates, target):
    ans = []
    backTrackCombinationSum(candidates, target, ans, [], 0, 0)
    return ans

def backTrackCombinationSum(candidates, target, ans, current, sum_, index):
    if sum_ == target:
        ans.append(current[:])
    elif sum_ < target:
        for i in range(index, len(candidates)):
            current.append(candidates[i])
            backTrackCombinationSum(candidates, target, ans, current, sum_+candidates[i], i)
            current.pop()
    
    return

print(combinationSum([2,3,6,7], 7))