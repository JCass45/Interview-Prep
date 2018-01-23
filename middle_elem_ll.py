class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def find_middle_elem(self):
        lag = self.head
        curr = self.head
        lag_index = 0
        curr_index = 0

        while curr:
            if lag_index < curr_index // 2:
                lag = lag.next
                lag_index += 1

            curr = curr.next
            curr_index += 1

        return lag.val

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == '__main__':
    linked_list = LL()
    linked_list.insert_node(1)
    linked_list.insert_node(2)
    linked_list.insert_node(3)
    linked_list.insert_node(4)
    linked_list.insert_node(5)
    print(linked_list.find_middle_elem())
