from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

    def __repr__(self):
        return str(self.val)


class Graph:
    def __init__(self):
        self.nodes = []

    def bfs(self, search_val, root):

        queue = deque()
        visited = [root]
        if root.val == search_val:
            return True, visited

        queue.append(root)
        while queue:
            r = queue.popleft()
            for neighbour in r.neighbours:

                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                if neighbour.val == search_val:
                    return True, visited

        return False, visited


def main():
    graph = Graph()
    graph.nodes.append(Node(1))
    graph.nodes.append(Node(2))
    graph.nodes.append(Node(3))
    graph.nodes.append(Node(4))
    graph.nodes.append(Node(5))
    graph.nodes.append(Node(6))
    graph.nodes[0].neighbours.append(graph.nodes[1])
    graph.nodes[0].neighbours.append(graph.nodes[4])
    graph.nodes[1].neighbours.append(graph.nodes[2])
    graph.nodes[1].neighbours.append(graph.nodes[3])
    graph.nodes[2].neighbours.append(graph.nodes[4])
    graph.nodes[4].neighbours.append(graph.nodes[5])
    found, path = graph.bfs(2, graph.nodes[0])
    print(found, path)


if __name__ == '__main__':
    main()
