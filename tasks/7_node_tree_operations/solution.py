from typing import Any


# Single node tree
class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


# Single Linked List
class LinkedNodeList:
    def __init__(self, head: Node = None):
        self.head = head

    def linked_list_as_list_of_values(self):
        result_list = []
        current_node = self.head
        while current_node:
            result_list.append(current_node.data)
            current_node = current_node.next_node
        return result_list

    def linked_list_size(self):
        size = 0
        if self.head is not None:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next_node
        return size

    def reverse_linked_node_list(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        return prev_node

    # Insertions:
    def insert_node_at_beginning(self, node_data: Any):
        new_node = Node(data=node_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_node_to_the_end(self, node_data: Any):
        new_node = Node(data=node_data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def insert_node_by_position(self, node_data: Any, index: int):
        new_node = Node(data=node_data)
        current_node = self.head
        current_position = 0
        if current_position == index:
            self.insert_node_at_beginning(node_data)
        else:
            while current_node is not None and current_position + 1 != index:
                current_position += 1
                current_node = current_node.next_node

            if current_node is not None:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
            else:
                raise ValueError("Index error.")

    # Removals:
    def remove_first_node(self):
        if self.head is not None:
            self.head = self.head.next_node

    def remove_last_node(self):
        prev_node = None
        if self.head:
            current_node = self.head
            while current_node.next_node:
                prev_node = current_node
                current_node = current_node.next_node
            prev_node.next_node = None

    def remove_node_by_position(self, index: int):
        if self.head is not None:
            current_node = self.head
            current_position = 0
            if current_position == index:
                self.remove_first_node()
            else:
                while current_node is not None and current_position + 1 != index:
                    current_position += 1
                    current_node = current_node.next_node

                if current_node is not None:
                    current_node.next_node = current_node.next_node.next_node
                else:
                    raise ValueError("Index error.")

    def update_node_by_position(self, new_node_data: Any, index: int):
        if self.head is not None:
            current_node = self.head
            current_position = 0
            if current_position == index:
                current_node.data = new_node_data
            else:
                while current_node is not None and current_position + 1 != index:
                    current_position += 1
                    current_node = current_node.next_node

                if current_node is not None:
                    current_node.next_node.data = new_node_data
                else:
                    raise ValueError("Index error.")

    def find_middle_element_additional_list(self):
        nodes_data = []
        current_node = self.head
        while current_node:
            nodes_data.append(current_node.data)
            current_node = current_node.next_node
        return nodes_data[len(nodes_data)//2]

    def find_middle_element_2_pointers(self):
        """
        2 pointers: fast and slow.
        increase fast pointer value by 2 and slow by 1, when fast pointer is None, slow is on middle node.
        """
        fast_pointer, slow_pointer = self.head, self.head
        while fast_pointer is not None and fast_pointer.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        return slow_pointer.data

    def merge_second_list_one_by_one(self, second_list_head: Node):
        original_pointer = self.head
        other_pointer = second_list_head

        while original_pointer is not None and other_pointer is not None:
            original_next = original_pointer.next_node
            other_next = other_pointer.next_node

            other_pointer.next_node = original_next
            original_pointer.next_node = other_pointer

            original_pointer = original_next
            other_pointer = other_next

