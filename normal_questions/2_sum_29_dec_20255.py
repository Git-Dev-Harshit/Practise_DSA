class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        found_at = []
        n = len(nums)
        
        for i in range(0, n):
            for j in range(i+1, n):

                if (nums[i] + nums [j] == target):
                    found_at.append(i)
                    found_at.append(j)
                    return found_at
               

if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([1,2,3], 5))