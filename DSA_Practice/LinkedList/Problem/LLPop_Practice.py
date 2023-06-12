# LL: Pop
# Your task is to implement the pop method for the LinkedList class.
#
# The pop method should remove the last node (tail) from the linked list and return the removed node. If the list is
# empty, the method should return None.
#
# After the last node is removed, the second-to-last node should become the new tail of the list.
#
# Additionally, if the list becomes empty after the pop operation, both the head and tail attributes should be set to
# None.
#
#
#
# Keep in mind the following requirements:
#
#
#
# The method should handle the cases where the list is empty, has only one node, or has multiple nodes.
#
# The method should update the tail attribute of the LinkedList correctly.
#
# The method should update the length attribute of the LinkedList to reflect the removal of the node.
#
# The method should either return the removed node or None if the list is empty.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""