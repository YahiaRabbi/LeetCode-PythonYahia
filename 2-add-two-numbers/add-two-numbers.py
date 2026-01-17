# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0  #one can be none
            value2 = l2.val if l2 else 0

            #new
            sum = value1 + value2 + carry  #for 2 digit numbers, we need carry
            carry = sum//10                #for 18, this gives 1
            sum = sum % 10                 # this gives 8
            current.next = ListNode(sum)

            #pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next





        