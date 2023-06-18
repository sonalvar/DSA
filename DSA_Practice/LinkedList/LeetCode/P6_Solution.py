class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        working_pointer = dummy.next
        while working_pointer.next is not None:
            node_to_be_extracted = working_pointer.next
            working_pointer.next = node_to_be_extracted.next
            node_to_be_extracted.next = dummy.next
            dummy.next = node_to_be_extracted
        head = dummy.next
        return head
