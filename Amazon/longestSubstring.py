# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#https://www.youtube.com/watch?v=BBAOiJp_EH4    ---> SLIDING WINDOW METHOD

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        char_set=set()
        start=0
        max_length=0
        index=0
        count=0
        while index < len(s):
            if s[index] not in char_set:
                char_set.add(s[index])
                index=index+1
                count+=1
            else:
                count=count-1
                #if s[start] in char_set:
                char_set.remove(s[start])
                start=start+1
            max_length=max([max_length,count])
        return max_length


s = "pwwke"
print Solution().lengthOfLongestSubstring(s)