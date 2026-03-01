# https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=array

class Solution:
    def maxArea(self, height: list[int]) -> int:
        final_sum = 0

        for i in range(len(height)):
            left_index = 0
            right_index = 0
            total_length = len(height) - 1
            actual_value = height[i]

            for left in range(0, i + 1):
                if actual_value <= height[left]:
                    left_index = left 
                    break

            while total_length >= i:
                if actual_value <= height[total_length]:
                    right_index = total_length
                    break
                total_length -= 1 

            sum = actual_value * (right_index - left_index)
            
            if sum > final_sum:
                final_sum = sum

        return final_sum

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))


# def maxArea(height: list[int]) -> int:
#     left_index = 0
#     right_index = 0
#     actual_value = 0
#     final_sum = 0
    

#     for i in range(len(height)):
#         total_length = len(height) - 1
#         actual_value = height[i]

#         for left in range(0, i + 1):
#             if actual_value <= height[left]:
#                 left_index = left 
#                 break

#         while total_length >= i:
#             if actual_value <= height[total_length]:
#                 right_index = total_length
#                 break
#             total_length -= 1 

#         # print('actual value : ', actual_value)
#         # print('left index : ', left_index, 'left value : ', height[left_index])
#         # print('right index : ', right_index, 'right value : ', height[right_index])
#         sum = actual_value * (right_index - left_index)
#         # print('sum : ', sum)
        
#         if sum > final_sum:
#             final_sum = sum
#         left_index = 0
#         right_index = 0
#         # print('-'*30)

#     return final_sum

# print(maxArea([1,8,6,2,5,4,8,3,7]))



