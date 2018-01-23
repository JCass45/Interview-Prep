from random import randrange

'''
Clone a LL given a random node
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class LL:
    def __init__(self):
        self.head = None
        self.nodes = {}

    def insert_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            index = 0
            while curr.next:
                curr = curr.next
                index += 1

            curr.next = new_node
            self.nodes[index] = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, curr.random.val)
            curr = curr.next

    def randomise_pointers(self):
        if self.head is None:
            return

        curr = self.head
        while curr:
            curr.random = self.nodes[randrange(len(self.nodes.keys()))]
            curr = curr.next

    def clone_list(self):
        new_list = LL()
        curr = self.head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        curr = self.head
        copy = curr.next
        new_list.head = copy
        while curr:
            curr.next.random = curr.random.next
            curr.next = copy.next
            curr = copy.next
            if curr:
                copy = curr.next

        return new_list


if __name__ == '__main__':
    linked_list = LL()
    linked_list.insert_node(1)
    linked_list.insert_node(2)
    linked_list.insert_node(3)
    linked_list.insert_node(4)
    linked_list.insert_node(5)
    linked_list.randomise_pointers()
    print('Original List')
    linked_list.print_list()
    new_linked_list = linked_list.clone_list()
    print('New list')
    new_linked_list.print_list()
    print('Original List')
    linked_list.print_list()
