# https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=array


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]

        for i in range(1, len(strs)):
            str1 = result
            str2 = strs[i]
            new_str = []
            max_len = min(len(str1), len(str2))

            for k in range(max_len):
                if str1[k] == str2[k]:
                    new_str.append(str1[k])
                else:
                    break

            result = "".join(new_str)

        return result
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))



# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
