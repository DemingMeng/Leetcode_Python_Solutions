import bisect
class Solution:
    def return_ans(self,ans,lis,target):
        if len(lis)<=1:
            return 0
        if target<lis[0] or target>lis[-1]:
            return 0
        if target==lis[0]:
            if lis[0]==lis[1]:
                ans.append([int(-target*2),lis[0],lis[1]])
            return 0
        target_index = bisect.bisect(lis,target)
        if target==lis[target_index-1]:
            target_index = target_index-1
        left=target_index-1
        right= target_index
        while True:
            if(right>(len(lis)-1)or left<0):
                return 0
            else:
                    if lis[left]+lis[right]==target*2:
                        ans.append([int(-target*2),lis[left],lis[right]])
                    if lis[left]+lis[right]<=target*2:
                        right +=1
                    else:
                        left -=1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums)<=2:
            return []
        if nums[-1]<0 or nums[0]>0:
            return []
        ans = []
        zero_index = bisect.bisect(nums,0)
        for i in range(zero_index):
            self.return_ans(ans,nums[i+1:],-nums[i]/2)
        ans_=[]
        for j in ans :
            if j not in ans_:
                ans_.append(j)
        return ans_