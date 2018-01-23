class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

    def __repr__(self):
        return str(self.val)


class Graph:
    def __init__(self):
        self.nodes = []

    def dfs(self, search_val, root, visited=[]):
        visited.append(root)
        if root.val == search_val:
            return True

        found = False
        for neighbour in root.neighbours:
            if neighbour not in visited and not found:
                found = self.dfs(search_val, neighbour, visited)

        return found


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
    visited = []
    print(graph.dfs(6, graph.nodes[0], visited))
    print(visited)


if __name__ == '__main__':
    main()
