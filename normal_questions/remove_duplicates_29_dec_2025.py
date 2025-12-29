class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        unique = []
        duplicate = []
        final_nums = []

        for i in range(0, n):
            if(nums[i] in unique):
                continue
            unique.append(nums[i])
            for j in range (i+1, n):
                if(nums[i]==nums[j]):
                    duplicate.append(nums[j])

        final_nums = unique + duplicate

        for i in range(0, len(final_nums)):
            nums[i] = final_nums[i]

        return len(unique)


if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([1,2,3,4,5,6,6,7]))