# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        largest_char = None
        largest_count = 0
        dict = {}

        for char in S:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
            if largest_count < dict[char]:
                largest_char = char
                largest_count = dict[char]
        # print largest_char,largest_count

        if largest_count -1 > (len(S) - largest_count):
            return ""

        result = [largest_char for i in range(largest_count)]  # ex ['a', 'a', 'a', 'a']

        del dict[largest_char]
        k = 0

        for char in dict:
            while dict[char] > 0:
                result[k] += char
                dict[char] -= 1
                k += 1

                if k == len(result):
                    k = 0

        return "".join(result)



S = "aaaabbbcc"
print Solution().reorganizeString(S)