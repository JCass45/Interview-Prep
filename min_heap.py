from math import log


class Heap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def remove_min(self):
        if len(self.heap) == 0:
            raise ValueError

        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down()
        return min_item

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up()

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            self.heap[smaller_child_index], self.heap[index] = self.heap[index], self.heap[smaller_child_index]
            index = smaller_child_index

    def heapify_up(self):
        index = len(self.heap) - 1
        item = self.heap[index]
        while self.has_parent(index) and self.parent(index) > item:
            self.heap[self.get_parent_index(
                index)], self.heap[index] = self.heap[index], self.heap[self.get_parent_index(index)]
            index = self.get_parent_index(index)

    def print_heap(self):
        printed_items = 1
        for item in self.heap:
            print(item, end=' ')
            printed_items += 1
            if log(printed_items, 2) % 1 == 0:
                print('\n')

        print(self.heap)


def main():
    heap = Heap()
    heap.insert(2)
    heap.insert(3)
    heap.insert(8)
    heap.insert(4)
    heap.insert(7)
    heap.insert(10)
    heap.insert(9)
    heap.print_heap()


if __name__ == '__main__':
    main()
