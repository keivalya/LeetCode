from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                print(nums[i]+nums[j])
                if i != j:
                    if nums[i]+nums[j] == target:
                        return [i,j]
        return None