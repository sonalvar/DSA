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

    def delete_n_nodes_after_m_nodes(self, m, n):
        temp = self.head
        for _ in range(m):
            temp = temp.next
        previous = temp
        for _ in range(n):
            # after = temp.next
            # temp.next = temp.next.next
            # after.next = None
            temp = temp.next
        after = temp.next
        if after is None:
            previous.next = None
            self.tail = previous
        else:
            previous.next = temp.next
            temp.next = None


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_list()

print("------------------------------------")
linked_list.delete_n_nodes_after_m_nodes(1, 3)
linked_list.print_list()
print("****************************")
print(linked_list.head.value)
print(linked_list.tail.value)
