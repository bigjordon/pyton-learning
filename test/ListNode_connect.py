# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
        def addTwoNumbers(self, l1, l2):
                rp = ListNode(0)
                rhead = rp
                carry = 0
                pl1 = l1
                pl2 = l2

                while pl1 != None and pl2 != None :
                        lsum = carry + pl1.val + pl2.val
                        rp.next = ListNode(lsum % 10)
                        carry = lsum // 10
                        rp = rp.next
                        pl1 = pl1.next
                        pl2 = pl2.next

                if pl1 == None :
                        plt = pl2
                elif pl2 == None :
                        plt = pl1
                while plt != None :
                        lsum = carry + plt.val
                        rp.next = ListNode(lsum % 10)
                        carry = lsum // 10
                        rp = rp.next 
                        plt = plt.next 
                if carry : 
                        print(carry) 
                        rp.next = ListNode(carry)
                return rhead.next 
l1 = ListNode(0) 
head1  = l1 
print(head1.next) 
print(id(head1.next))  # same 
print(id(None))        # same 
l1 =  l1.next 
print(head1.next) 
 
 
l2 = ListNode(0) 
head2 = l2 
print(head2.next) 
l2.next = ListNode(0) 
l2 = l2.next 
print(head2.next)
