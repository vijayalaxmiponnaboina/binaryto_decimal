class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        num=0
        while curr:
            num=num*2+curr.val
            curr=curr.next
        return num