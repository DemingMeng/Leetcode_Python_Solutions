# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Heapify(self,lis,index):
        length = len(lis)
        if 2*index+1>=length:
            pass
        else:
                if 2*index+2<length:
                    if lis[index][0]>max(lis[2*index+1][0],lis[2*index+2][0]):
                        pass
                    else:
                        if lis[2*index+2][0]>lis[2*index+1][0]:
                            a = lis[2*index+2]
                            lis[2*index+2] = lis[index]
                            lis[index]=a
                            self.Heapify(lis,2*index+2)
                        else:
                            a = lis[2*index+1]
                            lis[2*index+1] = lis[index]
                            lis[index]=a
                            self.Heapify(lis,2*index+1)
                else:
                     if lis[index][0]>lis[2*index+1][0]:
                        pass
                     else:
                        a = lis[2*index+1]
                        lis[2*index+1] = lis[index]
                        lis[index]=a

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [i for i in lists if i !=None]
        value_index_list = [[-lists[i].val,i] for i in range(len(lists))]
        for j in range(int(len(lists)/2)-1,-1,-1):
            self.Heapify(value_index_list,j)
        Start=ListNode()
        root = Start
        count,length_lists = 0,len(lists)
        while count !=length_lists:
            value=value_index_list[0][0]
            index = value_index_list[0][1]
            Start.next = ListNode(-value)
            Start = Start.next
            if lists[index].next!=None:
                value_index_list[0][0] =-(lists[index].next.val)
            else:
                value_index_list[0][0] = - 100000
                count +=1
            lists[index] =  lists[index].next
            self.Heapify(value_index_list,0)
        return root.next
"""Using Minimum Heap, time complexity is nlog(k), n is the sum of length of K Lists"""