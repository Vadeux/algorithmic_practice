from solution import Node, LinkedNodeList


node_5 = Node(data=5)
node_4 = Node(data=4, next_node=node_5)
node_3 = Node(data=3, next_node=node_4)
node_2 = Node(data=2, next_node=node_3)
node_1 = Node(data=1, next_node=node_2)

# 1 - Create linked node list.
linked_node_list = LinkedNodeList(head=node_1)

# 2 - Get linked node list as list of values.
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5]

# 3 - Get size of inked node list.
assert linked_node_list.linked_list_size() == 5

# 4 - Reverse linked node list.
linked_node_list.reverse_linked_node_list()
assert linked_node_list.linked_list_as_list_of_values() == [5, 4, 3, 2, 1]

# 4 - Reverse linked node list (restore changes in the list).
linked_node_list.reverse_linked_node_list()
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5]

# 6 - Insert node at list beginning.
linked_node_list.insert_node_at_beginning(node_data=0)
assert linked_node_list.linked_list_as_list_of_values() == [0, 1, 2, 3, 4, 5]

# 7 - Remove first node.
linked_node_list.remove_first_node()
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5]

# 8 - Insert node at list ending.
linked_node_list.insert_node_to_the_end(6)
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5, 6]

# 8 - Remove last node.
linked_node_list.remove_last_node()
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5]

# 9 - Insert node by position.
linked_node_list.insert_node_by_position(node_data=999, index=2)
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 999, 3, 4, 5]

# 10 - Remove node by position.
linked_node_list.remove_node_by_position(index=2)
assert linked_node_list.linked_list_as_list_of_values() == [1, 2, 3, 4, 5]

# 11 - Update node by position.
linked_node_list.update_node_by_position(999, 1)
assert linked_node_list.linked_list_as_list_of_values() == [1, 999, 3, 4, 5]

# 12 - Find middle node list element.
assert linked_node_list.find_middle_element_additional_list() == 3

# 12 - Find middle node list element.
assert linked_node_list.find_middle_element_2_pointers() == 3

# 13 - Merge Second node list into original.
original_node_5 = Node(data=5)
original_node_4 = Node(data=4, next_node=original_node_5)
original_node_3 = Node(data=3, next_node=original_node_4)
original_node_2 = Node(data=2, next_node=original_node_3)
original_node_1 = Node(data=1, next_node=original_node_2)
original_linked_node_list = LinkedNodeList(head=original_node_1)

node_55 = Node(data=55)
node_44 = Node(data=44, next_node=node_55)
node_33 = Node(data=33, next_node=node_44)
node_22 = Node(data=22, next_node=node_33)
node_11 = Node(data=11, next_node=node_22)
linked_node_list2 = LinkedNodeList(head=node_11)
original_linked_node_list.merge_second_list_one_by_one(linked_node_list2.head)
assert original_linked_node_list.linked_list_as_list_of_values() == [1, 11, 2, 22, 3, 33, 4, 44, 5, 55]
