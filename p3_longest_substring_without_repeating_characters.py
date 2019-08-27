# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

import queue
q = queue.Queue()

class Solution:
    def lengthOfLongestSubstringV2(self, s):
        charDict = {}
        startIndex = 0
        maxLen = 0
        for i, char in enumerate(s):
            if char in charDict and charDict[char] >= startIndex:
                startIndex = charDict[char] + 1
            charDict[char] = i
            currLen = i - startIndex + 1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen


    def lengthOfLongestSubstring(self, s):
        q = queue.Queue()
        charDict = {}
        maxLen = 0
        currLen = 0
        for char in s:
            # if charDict.has_key(char):
            if char in charDict:
                self.dropCharacters(q, charDict, char)
            q.put(char)
            charDict[char] = 0
            currLen = q.qsize()
            if currLen > maxLen:
                maxLen = currLen
        return maxLen


    def dropCharacters(self, q, charDict, char):
        while not q.empty():
            c = q.get()
            del charDict[c]
            if c == char:
                break




if __name__ == '__main__':
    test_str = 'abba'
    solution = Solution()
    result = solution.lengthOfLongestSubstringV2(test_str)
    print(result)