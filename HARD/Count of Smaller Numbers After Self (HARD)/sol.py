from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, indexes):
            if len(nums) <= 1:
                return nums, indexes

            mid = len(nums) // 2
            left, left_indexes = mergeSort(nums[:mid], indexes[:mid])
            right, right_indexes = mergeSort(nums[mid:], indexes[mid:])

            merged = []
            merged_indexes = []
            i, j = 0, 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    merged_indexes.append(left_indexes[i])
                    res[left_indexes[i]] += right_count
                    i += 1
                else:
                    merged.append(right[j])
                    merged_indexes.append(right_indexes[j])
                    right_count += 1
                    j += 1

            while i < len(left):
                merged.append(left[i])
                merged_indexes.append(left_indexes[i])
                res[left_indexes[i]] += right_count
                i += 1

            while j < len(right):
                merged.append(right[j])
                merged_indexes.append(right_indexes[j])
                j += 1

            return merged, merged_indexes

        res = [0] * len(nums)
        indexes = list(range(len(nums)))
        mergeSort(nums, indexes)

        return res
