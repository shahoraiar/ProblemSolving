# https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=array

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        marge = nums1 + nums2
        marge = sorted(marge)
        if len(marge)%2 == 0:
            middle = (marge[int(len(marge)/2)] + marge[int(len(marge)/2) - 1]) / 2

            return middle
        else:
            return marge[int(len(marge)/2)]

obj = Solution()
print(obj.findMedianSortedArrays([1,2], [3,4]))

def findMedianSortedArrays(num1:list[int], num2:list[int]) -> float:
    marge = num1 + num2
    marge = sorted(marge)
    if len(marge)%2 == 0:
        middle = (marge[int(len(marge)/2)] + marge[int(len(marge)/2) - 1]) / 2
        return middle
    else:
        return marge[int(len(marge)/2)]

print(findMedianSortedArrays([1,2], [3,4]))


