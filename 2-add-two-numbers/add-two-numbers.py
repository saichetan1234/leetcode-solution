# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp = l1
        b = []
        while(temp!=None):
            b.append(temp.val)
            temp = temp.next
        print(b)

        c = []
        i = len(b)-1
        while(i>=0):
            c.append(b[i])
            i = i-1
        print(c)

        number1 = int(''.join(map(str,c)))
        print(number1)



        temp1 = l2
        e = []
        while(temp1!=None):
            e.append(temp1.val)
            temp1 = temp1.next
        print(e)

        f = []
        j = len(e)-1
        while(j>=0):
            f.append(e[j])
            j = j-1
        print(f)

        number2 = int(''.join(map(str,f)))
        print(number2)

        number3 = number1 + number2
        print(number3)

        list1 = list(map(int,str(number3)))

        print(list1)

        list2 = list1[::-1]
        print(list2)

        dummy = ListNode(0)
        curr = dummy

        for i in list2:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        
        