from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTree:
    def __init__(self, root):
        self.root = root

    def add_node(self, curr_node, val):
        if val <= curr_node.val:
            if curr_node.left:
                self.add_node(curr_node.left, val)
            else:
                curr_node.left = Node(val)
        elif val > curr_node.val:
            if curr_node.right:
                self.add_node(curr_node.right, val)
            else:
                curr_node.right = Node(val)

    def print_by_level(self):
        if not self.root:
            return

        current_level = deque()
        next_level = deque()
        current_level.append(self.root)

        while len(current_level) > 0:
            curr_node = current_level.popleft()
            if curr_node:
                print(curr_node.val, end=' ')
                next_level.append(curr_node.left)
                next_level.append(curr_node.right)

            if len(current_level) == 0:
                print('')
                tmp = current_level
                current_level = next_level
                next_level = tmp


if __name__ == '__main__':
    my_tree = BTree(Node(9))
    my_tree.add_node(my_tree.root, 2)
    my_tree.add_node(my_tree.root, 10)
    my_tree.add_node(my_tree.root, 1)
    my_tree.add_node(my_tree.root, 7)
    my_tree.add_node(my_tree.root, 11)
    my_tree.print_by_level()
