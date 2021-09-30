class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        if (len(s) <= 1):
            return 1
        if (len(s) <= 2):
            if s[0] == s[1]:
                return 1
            else:
                return 2
        if (len(s) <= 3):
            if (s[0] == s[1]) and (s[1] == s[2]):
                return 1
            if (s[0] != s[1]) and (s[1] != s[2]) and (s[2] != s[0]):
                return 3
            return 2
        midium = int(len(s) / 2)
        l1 = s[:midium]
        l2 = s[midium:]
        l2_index = len(l2)

        l1_index = -len(l1)
        for i in range(1, len(l2)):
            if l2[:i].find(l2[i]) != -1:
                l2_index = i
                break
        for i in range(1, len(l1)):
            if l1[-i:].find(l1[-i - 1]) != -1:
                l1_index = -i
                break
        l1_new = l1[l1_index:]
        l2_new = l2[:l2_index]
        l3 = []
        l4 = [len(l2_new)]
        print(l2_new)
        for j in range(1, len(l1_new) + 1):
            a = l2_new.find(l1_new[-j])
            if a == -1:
                a = len(l2_new)
                a = min(min(l4), a)
                l3.append(a + j)
            else:
                l4.append(a)
                a = min(min(l4), a)
                l3.append(a + j)
        print(l3)
        b = max(l3)
        return max(b, self.lengthOfLongestSubstring(l1), self.lengthOfLongestSubstring(l2))