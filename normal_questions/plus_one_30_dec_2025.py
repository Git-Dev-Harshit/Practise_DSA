class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        result_list = []

        for i in range(0, len(digits)):
            sum = digits[i] + sum * 10
        
        sum = sum + 1

        while(sum>0):
            last = sum % 10
            sum = sum //10
            result_list.append(last)
        
        return result_list[::-1]


if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([1,2,5]))