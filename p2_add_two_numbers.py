class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class Solution:
    def __init__(self):
        self.input1 = None
        self.input2 = None
        self.input1Array = [2, 4, 3]
        self.input2Array = [5, 6, 4]
    
    def initList(self):
        operator = self.input1
        for x in self.input1Array:
            node = ListNode(x)
            if self.input1 is None:
                self.input1 = node
                operator = node
            else:
                operator.next = node
                operator = node

        operator = self.input2
        for x in self.input2Array:
            node = ListNode(x)
            if self.input2 is None:
                self.input2 = node
                operator = node
            else:
                operator.next = node
                operator = node

    def addTwoNumbers(self, l1, l2):
        operator = l1
        strNum1 = ''
        while operator:
            strNum1 += str(operator.val)
            operator = operator.next
        strNum1 = strNum1[::-1]

        strNum2 = ''
        operator = l2
        while operator:
            strNum2 += str(operator.val)
            operator = operator.next
        strNum2 = strNum2[::-1]

        strResult = str(int(strNum1) + int(strNum2))[::-1]

        header = None
        operator = None
        for s in strResult:
            node = ListNode(int(s))
            if header is None:
                header = node
                operator = node
            else:
                operator.next = node
                operator = node
        return header

    def addTwoNumbersV2(self, l1, l2):
        carry = 0
        resultHeader = None
        resultOperator = None
        while l1 is not None or l2 is not None:
            value = 0
            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next
            value += carry
            carry = 0
            if value >= 10:
                carry = 1
                value -= 10
            node = ListNode(value)
            if resultHeader is None:
                resultHeader = node
                resultOperator = node
            else:
                resultOperator.next = node
                resultOperator = node
        if carry == 1:
            node = ListNode(1)
            resultOperator.next = node
        return resultHeader
    
    # 学习别人的写法，代码简洁，漂亮, 但是发现速度不是最快的
    def addTwoNumbersV3(self, l1, l2):
        header = ListNode(0)
        operator = header
        carry = 0
        while carry or l1 or l2:
            carry, remainder = divmod(carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            operator.next = ListNode(remainder)
            operator = operator.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return header.next




if __name__ == '__main__':
    solution = Solution()
    solution.initList()
    header = solution.addTwoNumbersV3(solution.input1, solution.input2)
    while header:
        print(header.val)
        header = header.next