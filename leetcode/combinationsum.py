class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = [[] for i in range(0, target + 1)]
        for i in candidates:
            if i > target:
                pass
            else:
                l[i].append([i])
        for j in range(1, target + 1):
            for k in range(0, int(j / 2) + 1):
                for left in l[k]:
                    for right in l[j - k]:
                        ans = left + right
                        if ans == []:
                            pass
                        else:
                            not_in = True
                            for i in l[j]:
                                if len(ans) == len(i):
                                    l_left = {}
                                    l_right = {}
                                    for ii in ans:
                                        if ii in l_left.keys():

                                            l_left[ii] += 1
                                        else:
                                            l_left[ii] = 1
                                    for ii in i:
                                        if ii in l_right.keys():
                                            l_right[ii] += 1
                                        else:
                                            l_right[ii] = 1
                                    if l_left == l_right:
                                        not_in = False
                                        break
                            if not_in:
                                l[j].append(ans)

        return l[-1]