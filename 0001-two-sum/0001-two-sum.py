class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in pair_idx:
                return [i, pair_idx[target-num]]
            pair_idx[num] = i

        