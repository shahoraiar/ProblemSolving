class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                
num = eval(input())
target = eval(input())
# input : 
# 2,7,11,3
# 9
sol = Solution()
result = sol.twoSum(num , target)

print(result)