class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        l=[]
        for i in range(0,len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
                nums[k]=nums[i] 
                k+=1
        return k
        