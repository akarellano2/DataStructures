# Name: Ana Karen Arellano
# ID: 80631366
# Lab 5
# import matplotlib.pyplot as plt
import math


# heap class
class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = 0
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i += 1


class LRU:
    def __init__(self, capacity):
        self.LRU = {}
        self.capacity = capacity
        self.list = DoublyLL()
        self.size = 0

    def get(self, key):
        if key in self.LRU:
            self.list.relocate(self.LRU[key])
            return self.LRU[key]
        return -1

        # Method that will get value of key in the cache if it were to be there
        # Create base case of case in which the key were to not be there

    def put(self, key, value):
        node = Node(key, value)
        if key not in self.LRU:
            if self.size is not self.capacity:
                self.size = self.size + 1
                self.LRU[key] = node
                self.list.insert_at_start(node)
            else:
                self.LRU[key] = node
                self.list.delete_at_end()
                self.list.insert_at_start(node)
        else:
            self.list.relocate(self.LRU[key])
            self.list.start.value = value
        # method which inserts or replaces the value of key that has not been used
        # will call method max_capacity to check the limit --> if limit reached
        # then it will invalidate least recently used item

    def size_of_list(self):
        return self.size

        # Will deliver the number of key and value pairs that are currently
        # stored in the array

    def max_capacity(self):

        return self.capacity

        # Method that will return the maximum capacity of the cache
        # Will be done by checking how many spaces are left to be put in

    def print_list(self):
        n = self.list.start
        while n is not None:
            print(n.value, n.key)
            n = n.next

# node class


class Node:

    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLL:

    def __init__(self):
        self.start = None
        self.tail = None

    #
    def insert_at_start(self, new_node):
        if self.start is None:
            self.start = new_node
            self.tail = new_node
            return
        # new_node = Node(value)
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node

    def delete_at_end(self):
        if self.start is None:
            # print("The list has no element to delete")
            return
        if self.start.next is None:
            self.start = None
            return
        curr = self.start
        while curr.next is not None:
            curr = curr.next
        curr.prev.next = None

    def relocate(self, node):
        if node is self.start:
            return
        if node is self.tail:
            curr = self.tail.prev
            curr.next = None
            self.tail = curr
            self.insert_at_start(node)
        else:
            temp = node.next
            temp.prev = node.prev
            temp2 = node.prev
            temp2.next = temp
            self.insert_at_start(node)


def most_frequent(keys_array, k):
    dictionary_with_keys = {}
    for i in range(len(keys_array)):
        if keys_array[i] in dictionary_with_keys:
            dictionary_with_keys[keys_array[i]] = dictionary_with_keys[keys_array[i]] + 1
        else:
            dictionary_with_keys[keys_array[i]] = 1

    list_of_keys = []
    for value in dictionary_with_keys.values():
        list_of_keys.append(value)

    heap_sort(list_of_keys)
    print("List of keys:")
    print(list_of_keys)
    # MaxHeap.sort(list_of_keys)
    list_no_repeats = list()
    i = 0

    while i < len(list_of_keys):
        for p in dictionary_with_keys:
            if list_of_keys[i] == dictionary_with_keys[p]:
                list_no_repeats.append(p)
                i += 1

    if k < 0 or k > len(list_no_repeats):
        print("not a valid k")

    else:
        print("List of words:")
        for i in range(k):
            print(list_no_repeats[i])


def main():
    print("Part A")
    a = LRU(3)
    a.put("A", 2)
    a.put("B", 6)
    a.put("C", 8)
    a.put("d", 9)
    a.put("e", 6)
    a.put("f", 8)
    print("list of key and value:")
    a.print_list()
    print("")
    print("Part B")
    array_of_words = ["a", "e", "b", "e", "b", "d", "f", "a", "c", "e", "u", "a", "l"]

    most_frequent(array_of_words, 4)


main()
