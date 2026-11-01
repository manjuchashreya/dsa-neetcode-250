"""
Problem: Reverse Linked List
Platform: NeetCode 250 / LeetCode 206
Topic: Linked Lists (iterative pointer reversal)
Date: Oct 31
Status: Green

Goal: reverse a singly linked list; return the new head.

Pattern: walk the list with `curr`, flipping each node's `next` to point back
at `prev`. You need `next_node` saved BEFORE flipping, or you lose the rest of
the list.

The 4-step dance (order matters):
    next_node = curr.next   # 1. remember where to go next
    curr.next = prev        # 2. flip this node's link backwards
    prev = curr             # 3. advance prev
    curr = next_node        # 4. advance curr
When curr becomes None, `prev` is the new head.

Time:  O(n)
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: "ListNode | None") -> "ListNode | None":
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == "__main__":
    def build(vals):
        head = None
        for v in reversed(vals):
            head = ListNode(v, head)
        return head

    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    s = Solution()
    print(to_list(s.reverseList(build([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(to_list(s.reverseList(build([1, 2]))))            # [2, 1]
    print(to_list(s.reverseList(build([]))))                # []
