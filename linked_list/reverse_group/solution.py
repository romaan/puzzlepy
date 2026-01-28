# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from LinkedListReversal import reverse_linked_list
from ds_v1.LinkedList.LinkedList import ListNode

def reverse_k_groups(head: ListNode, k: int) -> ListNode:
    # Check there are at least k nodes
    node = head
    for _ in range(k):
        if not node:
            return head
        node = node.next

    # Reverse first k nodes
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # head is now the tail of the reversed block
    head.next = reverse_k_groups(curr, k)
    return prev

