class AVLNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0


class AVL:

    def __init__(self):
        self.root = None

    def avl_tree_get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def avl_tree_update_height(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        right_height = -1
        if self.right is not None:
            right_height = self.right.height
        self.height = max(left_height, right_height)

    def avl_tree_replace_child(self, current_child, new_child):
        if self.left == current_child:
            return self.avl_tree_set_child("left", new_child)
        elif self.right == current_child:
            return self.avl_tree_set_child("right", new_child)

    def avl_tree_rotate_right(self, node):
        left_right_child = node.left.right

        if node.parent is not None:
            node.parent.avl_tree_replace_child(node, node.left)

        else:
            self.root = node.left
            self.root.paren = None

        node.left.avl_tree_set_child("right", node)
        node.avl_tree_set_child(node, "left", left_right_child)

        return node.parent

    def avl_tree_rebalance(self, node):

        node.avl_tree_update_height()

        if node.avl_tree_get_balance() == -2:
            if node.avl_tree_right.get_balance() == 1:
                self.avl_tree_rotate_right(node.right)

            return self.avl_tree_rotate_left(node)

        elif node.avl_tree_get_balance() == 2:

            if node.left.avl_tree_get_balance() == -1:
                self.avl_tree_rotate_left(node.left)

            return self.avl_tree_rotate_right(node)

        return node

    def avl_tree_set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self

        self.avl_tree_update_height()
        return True

    def avl_tree_insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None

        else:
            curr = self.root
            while curr is not None:
                if node.key < curr.key:

                    if curr.left is None:
                        curr.left = node
                        node.parent = curr
                        curr = None
                    else:
                        curr = curr.left
                else:

                    if curr.right is None:
                        curr.right = node
                        node.parent = curr
                        curr = None
                    else:
                        curr = curr.right

            node = node.parent
            while node is not None:
                self.avl_tree_rebalance(node)
                node = node.parent

    def remove_node(self, node):
        if node is None:
            return False

        parent = node.parent

        if node.left is not None and node.right is not None:
            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left
            node.key = successor_node.key

            self.remove_node(successor_node)

            return True

        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

        elif node.left is not None:
            parent.replace_child(node, node.left)

        else:
            parent.replace_child(node, node.right)

        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True

    def avl_tree_search(self, data, curr):
        if not curr:
            return 0
        if curr.data == data:
            return 1
        if data < curr.data:
            return self.avl_search(data, curr.left)
        if data > curr.data:
            return self.avl_search(data, curr.right)
        return 0

