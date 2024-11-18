class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            middle = len(arr) // 2
            left = merge_sort(arr[:middle])
            right = merge_sort(arr[middle:])

            return merge(left, right)

        def merge(left, right):
            sorted_arr = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1

            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])

            return sorted_arr

        return merge_sort(nums)
