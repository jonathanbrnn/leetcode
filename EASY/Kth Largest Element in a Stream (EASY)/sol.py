# The solution below is utter garbage and has a terrible runtime, this is due to my lack of understanding of heaps.
# The code is going to be updated 05.09.2024 after I had some time to learn about heaps!

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
