from Node import Node


class LList(object):
    head = None

    def __init__(self, head=None):
        self.head = None

    # checks if is empty
    def is_empty(self):
        return self.head is None

    # adds to end of list
    def append(self, x):
        # Inserts x at end of list L
        if is_empty(self):
            self.head = Node(x)
            self.tail = self.head

        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next


