class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False

        first = second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
