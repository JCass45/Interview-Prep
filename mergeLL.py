class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_ll(heads):
    for i in range(len(heads) - 1):
        current = heads[i]
        while current.next:
            current = current.next

        current.next = heads[i + 1]

    return heads[0]

def marge_k_ll_sorted(heads):
    


def main():
    heads = [ListNode(0) for i in range(5)]
    for i in range(5):
        current = heads[i]
        for j in range(1, 10):
            current.next = ListNode(j)
            current = current.next

    for i in range(len(heads)):
        current = heads[0]
        while current:
            print(current.val)
            current = current.next
        print('--------End of list {}---------'.format(i))

    new_list = merge_k_ll(heads)
    current = new_list
    while current:
        print(current.val)
        current = current.next


if __name__ == '__main__':
    main()
