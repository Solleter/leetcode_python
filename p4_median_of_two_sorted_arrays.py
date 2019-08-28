# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArraysV2(self, nums1, nums2):
        newList = sorted((nums1 + nums2))
        count = len(newList)
        index1 = -1
        index2 = -1
        if count % 2 == 0:
            index2 = int(count / 2)
            index1 = index2 - 1
            return (newList[index1] + newList[index2]) / 2.0
        else:
            index1 = int(count / 2)
            return newList[index1]

        

    def findMedianSortedArrays(self, nums1, nums2):
        count1 = len(nums1)
        count2 = len(nums2)
        all_count = count1 + count2
        index1 = -1
        index2 = -1

        if all_count % 2 == 0:
            index2 = int(all_count / 2)
            index1 = index2 - 1
        else:
            index1 = int(all_count / 2)

        print(all_count, index1, index2)

        count1 = -1 if count1 == 0 else count1
        count2 = -1 if count2 == 0 else count2

        print(count1, count2)

        num1 = 0
        num2 = 0
        i1 = 0
        i2 = 0
        currNum = 0
        sumNum = 0
        for i in range(0, all_count):
            if i1 < count1 and i2 < count2:
                if nums1[i1] < nums2[i2]:
                    currNum = nums1[i1]
                    i1 += 1
                else:
                    currNum = nums2[i2]
                    i2 += 1
            else:
                if i1 < count1:
                    currNum = nums1[i1]
                    i1 += 1
                elif i2 < count2:
                    currNum = nums2[i2]
                    i2 += 1
                else:
                    currNum = 0
            if i == index1:
                sumNum += currNum
            if i == index2:
                sumNum += currNum
        if index1 < 0 or index2 < 0:
            return sumNum
        else:
            return sumNum / 2

if __name__ == '__main__':
    solution = Solution()
    result = solution.findMedianSortedArraysV2([], [4,5, 6])
    print('Result: ', result)


        