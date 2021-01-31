class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.DFS(nums, S)
    
    def DFS(self, nums, S):
        ans = [0]
        self.DFSHelper(0, S, nums, 0, ans)
        return ans[0]
    
    def DFSHelper(self, current, target, arr, index, ans):
        
        if index >= len(arr):
            if current == target:
                ans[0] += 1
            return
        
        self.DFSHelper(current+arr[index], target, arr, index+1, ans)
        self.DFSHelper(current-arr[index], target, arr, index+1, ans)