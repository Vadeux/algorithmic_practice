from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node


def return_linked_list_values_as_list(head: ListNode) -> list:
    result_list = []
    while head:
        result_list.append(head.val)
        head = head.next
    return result_list


node_4 = ListNode(val=4)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
node_1 = ListNode(val=1, next=node_2)

assert return_linked_list_values_as_list(Solution.reverse_list(node_1)) == [4, 3, 2, 1]
