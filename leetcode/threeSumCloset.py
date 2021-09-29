class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=[]
        length = len(nums)
        ans = nums[0]+nums[1]+nums[2]
        minimum = nums[0]+nums[1]+nums[2]-target
        if minimum<0:
            minimum = -minimum
        for i in range(length-2):
            left,right = i+1,length-1
            new_target = target-nums[i]
            while right!=left:
                if nums[right]+nums[left]>new_target:
                    if minimum>nums[right]+nums[left]-new_target:
                        minimum=nums[right]+nums[left]-new_target
                        ans = nums[i]+nums[right]+nums[left]
                    right = right-1
                else:
                    if minimum>-nums[right]-nums[left]+new_target:
                        minimum=-nums[right]-nums[left]+new_target
                        ans = nums[i]+nums[right]+nums[left]
                    left = left+1
        return ans