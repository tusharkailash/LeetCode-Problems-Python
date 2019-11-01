import collections

class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        # print count                           #Counter({'i': 2, 'love': 2, 'coding': 1, 'leetcode': 1})
        words = count.keys()
        # print words                                #['i', 'coding', 'love', 'leetcode']
        words.sort(key = lambda i: (-count[i], i))

        return words[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print Solution().topKFrequent(words,k)


# to test lambda
        # for i in count:
        #     key=  lambda w: (count[w], w)
        #     print key(i)