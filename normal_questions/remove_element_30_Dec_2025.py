class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        valid = []
        not_valid = []
        final_list = []

        for i in range(0, len(nums)):
            if nums[i] == val:
                not_valid.append(nums[i])
            else:
                valid.append(nums[i])

        final_list = valid + not_valid

        for i in range(0, len(nums)):
            nums[i] = final_list[i]

        return len(valid)
    
if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([3,2,2,3], 3))