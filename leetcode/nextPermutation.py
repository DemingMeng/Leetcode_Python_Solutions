from bisect import bisect
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)<=1:
            pass
        else:
            last = nums[-1]
            counter  = 0
            for j in range(len(nums)):
                if nums[-j-1]>=last:
                    last  = nums[-j-1]
                    pass
                else:
                    l = nums[-j:]
                    l.sort()
                    index=bisect(l,nums[-j-1])
                    a = l[index]
                    l[index] =nums[-j-1]
                    nums[-j:]=l
                    nums[-j-1] = a
                    counter = 1
                    break
            if counter ==0:
                nums.sort()
"""Time complexity is nlog(n), constant space complexity requires writing a sort function with pointer"""