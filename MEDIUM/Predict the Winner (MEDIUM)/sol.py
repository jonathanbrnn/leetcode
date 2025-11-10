class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def minimax(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            pick_left = nums[left] - minimax(left + 1, right)

            pick_right = nums[right] - minimax(left, right - 1)

            best = max(pick_left, pick_right)

            memo[(left, right)] = best
            return best


        result = minimax(0, n - 1)

        return result >= 0
