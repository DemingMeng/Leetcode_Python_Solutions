class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if type(s)==str:
            array = []
            for i in range(len(s)):
                if s[i]=="(":
                    array.append(1)
                else:
                    array.append(-1)
        else:
            array = s
        length_array = len(array)
        if length_array<=1:
            return 0
        if length_array==2:
            if array==[1,-1]:
                return 2
            else:
                return 0
        midium = int(length_array/2)
        right = []
        left_sum,right_sum,left_minimum,right_minimum = 0,0,0,0
        ans ,length,ls = 0,0,0
        for i in range(midium,length_array):
            right_sum += array[i]
            right_minimum = min (right_sum,right_minimum)
            right.append(right_sum)
        for j in range (midium):
            left_sum +=array[midium-j-1]
            left_minimum = min(array[midium-j-1],left_minimum+array[midium-j-1])
            if (array[midium-j-1]==-1 or left_minimum<0):
                pass
            else:
                if left_sum+right_minimum<=0:
                    length,ls = j+1,left_sum
        for k in range(len(right)):
            if ls+right[k]==0:
                ans = k+1+length
            if ls+right[k]<0:
                break
        return max(ans,self.longestValidParentheses(array[:midium]),self.longestValidParentheses(array[midium:]))