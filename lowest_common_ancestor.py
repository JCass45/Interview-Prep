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

    def path_to_node(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return [val]

        left_path = self.path_to_node(root.left, val)
        if left_path is not None:
            left_path.append(root.val)
            return left_path

        right_path = self.path_to_node(root.right, val)
        if right_path is not None:
            right_path.append(root.val)
            return right_path

        return None

    def lowest_common_ancestor(self, root, val1, val2):
        path_val1 = self.path_to_node(root, val1)
        path_val2 = self.path_to_node(root, val2)
        last_popped = None
        while len(path_val1) > 0 and len(path_val2) > 0:
            popval1 = path_val1.pop()
            popval2 = path_val2.pop()
            if popval1 == popval2:
                last_popped = popval1
            else:
                break

        return last_popped


if __name__ == '__main__':
    my_tree = BTree(Node(9))
    my_tree.add_node(my_tree.root, 2)
    my_tree.add_node(my_tree.root, 10)
    my_tree.add_node(my_tree.root, 1)
    my_tree.add_node(my_tree.root, 7)
    my_tree.add_node(my_tree.root, 11)
    print(my_tree.lowest_common_ancestor(my_tree.root, 1, 7))
