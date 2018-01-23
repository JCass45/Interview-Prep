def build_max_heap(array):
    ''' Build a max heap in-place in provided array'''

    for i in range((len(array) // 2) - 1, -1, -1):
        max_heapify(array, i, len(array))


def max_heapify(array, i, max_index):
<<<<<<< HEAD
    # max_index arg needed for when we heapsort and we decrease the size of the heap relative to the input array
=======
>>>>>>> 61c40139a406b5635ae3f51fda60e93fe3aaec17
    while i < max_index:
        index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < max_index and array[left_child] > array[index]:
            index = left_child

        if right_child < max_index and array[right_child] > array[index]:
            index = right_child

        if index == i:
            # Neither child is greater than the parent
            break

        array[index], array[i] = array[i], array[index]

        i = index


def heapsort(array):
<<<<<<< HEAD
    '''
    1. Convert unsorted array to a max heap
    2. Repeat:
        Swap last and first index in max heap (first index is guaranteed largest element)
        Reconvert array into max heap, excluding the sorted portion (max heap becomes smaller by 1 element each time)
    '''
=======
>>>>>>> 61c40139a406b5635ae3f51fda60e93fe3aaec17
    build_max_heap(array)
    for last_index in range(len(array) - 1, -1, -1):
        array[0], array[last_index] = array[last_index], array[0]
        max_heapify(array, 0, last_index)


def main():
    heap = [5, 12, 91, 97, 37, 90, 64, 1]
    print('before:', heap)
    build_max_heap(heap)
    print('after', heap)
    heapsort(heap)
    print('sorted:', heap)


if __name__ == '__main__':
    main()
