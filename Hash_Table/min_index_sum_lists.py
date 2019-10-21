                        ### Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
#
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans = []
        dict = {v: i for i, v in
                enumerate(list1)}  # {'Tapioca Express': 1,'Shogun': 0,'KFC': 3,'Burger King':2} Basically key-val type
        min_sum = len(list1) + len(list2)

        for i, v in enumerate(list2):  # going over the second list
            if v not in dict:
                continue  # continue until a value is found in dict
            current_sum = i + dict[v]  # note the sum in a var to check it later with other matches

            if current_sum < min_sum:
                ans = [v]  # match with the minimum sum becomes the ans
                min_sum = current_sum
            elif current_sum == min_sum:
                ans.append(v)  # if all have same value, return all the results, thus do append
        return ans

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

print Solution().findRestaurant(list1,list2)



