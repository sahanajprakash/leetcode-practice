class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if (target - n) in m.keys():
                return [m[target - n], i]
            m[n] = i
        