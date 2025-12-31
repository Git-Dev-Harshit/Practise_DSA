class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}

        for n in nums:
            if n in counter.keys():
                current = counter[n]
                counter[n] = current+1
            else:
                counter[n] = 1
            
        for key, value in counter.items():
            if value == 1:
                return key
            
if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([2,1,2]))