# Linked Lists Notes

## Topic summary

Singly linked lists: nodes with `val` + `next`. Core skills — traversal,
reversing links, dummy nodes, and fast/slow (two-pointer) tricks.

## Problems solved

| Problem | Pattern | Status | Time | Space | Code |
| ------- | ------- | ------ | ---- | ----- | ---- |
| 206 Reverse Linked List | Iterative pointer reversal | 🟢 | O(n) | O(1) | `day09/01_reverse_linked_list.py` |

## The reversal dance (206)

Walk with `curr`, flipping each `next` back to `prev`. Save `next_node` BEFORE
flipping or you lose the rest of the list. Order matters:

```python
prev, curr = None, head
while curr:
    next_node = curr.next   # 1. remember the rest
    curr.next = prev        # 2. flip link backwards
    prev = curr             # 3. advance prev
    curr = next_node        # 4. advance curr
return prev                 # prev is the new head
```

## Linked-list toolkit (for upcoming problems)

- **Dummy node:** `dummy = ListNode(0, head)` — avoids special-casing the head
  when inserting/deleting (Merge Two Lists, Remove Nth From End).
- **Fast/slow pointers:** fast moves 2x, slow 1x. Finds the middle
  (Middle of the List), detects cycles (Linked List Cycle), and locates the
  nth-from-end.
- **Always check `None`:** every `curr.next` / `fast.next.next` can hit the end.
  Trace the empty list and single node before submitting.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
