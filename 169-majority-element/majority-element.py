class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]=d.get(i)+1
            else:
                d[i]=1
        n=len(nums)
        max_element = -1
        max_count = 0

        for k, v in d.items():
            if v > n / 3 and v > max_count:
                max_element = k
                max_count = v
        return max_element