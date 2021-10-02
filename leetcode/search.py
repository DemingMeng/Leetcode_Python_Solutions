from bisect import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 2:
            if target == nums[0]:
                return 0
            if target == nums[1]:
                return 1
            return -1
        a = nums[0]
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            key = bisect(nums, target)
            if nums[key - 1] == target:
                return key - 1
            else:
                return -1
        else:
            while left != right:
                index = int((left + right) / 2)

                if nums[index] >= a:
                    if right - left == 1:
                        left = right
                        break
                    left = index
                else:
                    if right - left == 1:
                        right = left
                        break
                    right = index
            k = left
            if target >= nums[0] and target <= nums[k - 1]:
                left, right = 0, k - 1
                while left != right:
                    index = int((left + right) / 2)
                    if target == nums[index]:
                        return index
                    if nums[index] > target:
                        if right - left == 1:
                            return -1
                        right = index
                    else:
                        if right - left == 1:
                            if nums[right] == target:
                                return right
                            else:
                                return -1
                        left = index
                return left
            else:
                if target >= nums[k] and target <= nums[-1]:
                    left, right = k, len(nums) - 1
                    while left != right:
                        index = int((left + right) / 2)
                        if target == nums[index]:
                            return index
                        if nums[index] > target:
                            if right - left == 1:
                                return -1
                            right = index
                        else:
                            if right - left == 1:
                                if nums[right] == target:
                                    return right
                                else:
                                    return -1

                            left = index
                    return left
                return -1
"""Time complexity is log(n)"""