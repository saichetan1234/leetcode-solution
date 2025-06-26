# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        b = []

        while(temp!=None):
            b.append(temp.val)
            temp = temp.next
        print(b)

        ans = {}
        c = []
        for i in b:
            ans[i] = ans.get(i,0) +1
        for key,value in ans.items():
            if value>=1:
                c.append(key)
        print(c)

        dummy = ListNode(0)
        curr = dummy

        for i in c:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next

            
        