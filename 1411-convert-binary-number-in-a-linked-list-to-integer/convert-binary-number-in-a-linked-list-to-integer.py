# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        temp = head
        b = []

        while temp!=None:
            b.append(temp.val)
            temp = temp.next
        print(b)

        ans = b[::-1]
        count = 0

        if len(ans) == 1:
            return ans[0]
            
        else:

            for i in range(len(ans)):
                if ans[i] ==1:
                    count = count + pow(2,i)
            return count
            
            