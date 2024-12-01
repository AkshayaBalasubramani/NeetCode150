class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        d={}
        for i in nums:
            if i in d.keys():
                d[i]=d.get(i)+1
            else:
                d[i]=1
        n=len(nums)
        for k,v in d.items():
            if v>n/3:
                ans.append(k)
        return ans
        