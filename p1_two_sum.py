class Solution:
	def twoSum(self, nums, target):
		dict = {}
		for i, num in enumerate(nums):
			minus_value = target - num
			if minus_value in dict and dict[minus_value] != i:
				return [dict[minus_value], i]
			dict[num] = i
		return []
		

if __name__ == '__main__':
	nums = [3, 3]
	target = 6
	solution = Solution()
	result = solution.twoSum(nums, target)
	print(result)