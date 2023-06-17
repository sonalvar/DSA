class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start, end):
        if start == end:
            return
        beg_flag = False
        if start == 0:
            beg_flag = True
        start += 1
        end += 1
        dummy = Node(0)
        dummy.next = self.head
        node_before_sublist = dummy
        for _ in range(start - 1):
            node_before_sublist = node_before_sublist.next
        working_pointer = node_before_sublist.next
        while start < end:
            node_to_be_extracted = working_pointer.next
            working_pointer.next = node_to_be_extracted.next
            node_to_be_extracted.next = node_before_sublist.next
            node_before_sublist.next = node_to_be_extracted
            start += 1
        if beg_flag:
            self.head = dummy.next
        return dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


print("Original linked list: ")
linked_list.print_list()
#
# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()
#
# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
print("Reversed empty linked list: ")
if empty_list.reverse_between(0, 0):
    print(empty_list.print_list())
else:
    print("None")



"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None

"""
