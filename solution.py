class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ans={}
        for i,num in enumerate(nums):
            ans=target-num
            if ans in dict_ans:
                return [dict_ans[ans],i]
            else:
                dict_ans[num]=i
