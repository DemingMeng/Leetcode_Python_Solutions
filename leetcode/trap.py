class Solution:
    def trap(self, height):
        left ,right= 0,1
        rain = 0
        if (len(height)<=1):
            return 0
        while right!=len(height):
            if height[right]>=height[left]:
                if ((right - left)-1)>0:
                    rain += ((right - left)-1)*height[left]
                    for i in range(left+1,right):
                        rain -=height[i]
                left = right
            right +=1
        if right -left<=1:
            return rain
        else:
            maximum,j= 0,left
            for i in range (left+1,len(height)):
                if height[i]>=maximum:
                    maximum=height[i]
                    j = i
            rain+= height[j]*(j-left-1)
            for k in range(left+1,j):
                rain-=height[k]
            else:
                return rain +self.trap(height[j:])