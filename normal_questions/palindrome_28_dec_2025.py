class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_number = 0
        number = x

        while(number > 0):
            last_number = number % 10
            number = number // 10
            reversed_number = last_number + reversed_number * 10
            
        if (x == reversed_number):
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(121))