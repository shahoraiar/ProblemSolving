# array hash_table
# proble : https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
            
num = eval(input())
target = eval(input())
# input : 
# 2,7,11,3
# 9
sol = Solution()
result = sol.twoSum(num , target)

print(result)


