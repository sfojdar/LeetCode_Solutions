class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        list=[]
        while i<len(nums):
            if nums[i] in list:
                nums.remove(nums[i])
            else:
                list.append(nums[i])
                i+=1
        return len(nums)