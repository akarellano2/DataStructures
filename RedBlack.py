
class RedBlackNode:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None
        self.color = "red"
        self.parent = None


class RedBlack:

    def __init__(self, root=None, height=-1):
        self.root = root

    def rbt_tree_replace_child(self, parent, curr_child, new_child):
        if parent.left == curr_child:
            return self.rbt_tree_set_child(parent, "left", new_child)
        elif parent.right == curr_child:
            return self.rbt_tree_set_child(parent, "right", new_child)
        return False

    def rbt_insert(self, data):
        node = Node(data)
        self._bst_insert(node)
        node.color = "red"
        self.rbt_balance(node)

    def _bst_insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return
        curr = self.root
        while cur is not None:
            if node.data < cur.data:
                if curr.left is None:
                    curr.left = node
                    node.parent = curr
                    curr = None
                else:
                    cur = cur.left
            else:
                if curr.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right

    def insertion_balance(self, node):
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.is_black():
            return
        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        if uncle is not None and uncle.is_red():
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.insertion_balance(grandparent)
            return
        if node is parent.right and parent is grandparent.left:
            self.rbt_tree_rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.rbt_tree_rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"

        if node is parent.left:
            self.rbt_tree_rotate_right(grandparent)
        else:
            self.rbt_tree_rotate_left(grandparent)

    def in_order(self, visitor_function):
        self.in_order_recursive(visitor_function, node)

    def in_order_recursive(self, visitor_function, node):
        if node is None:
            return
        self.in_order_recursive(visitor_function, node.left)
        visitor_function(node)
        self.in_order_recursive(visitor_function, node.right)

    def is_none_or_black(self, node):
        if node is None:
            return True
        return node.is_black

    def is_not_none_and_red(self, node):
        if node is None:
            return False
        return node.is_red()

    def rbt_tree_rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.parent.rbt_tree_replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent is None

        self.right.rbt_tree_set_child("left", node)
        self.rbt_tree_set_child("right", right_left_child)

    def rbt_tree_rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.parent.rbt_tree_replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None

        self.left.rbt_tree_set_child("right", node)
        self.rbt_tree_set_child("left", left_right_child)

    def rbt_tree_search(self, data, curr):
        if not curr:
            return 0
        if curr.data is data:
            return 1
        if data < curr.data:
            return self.rbt_tree_search(data, curr.left)
        if data > curr.data:
            return self.rbt_tree_search(data, curr.right)
        return 0

    def rbt_tree_try_case1(self, node):
        if node.is_red() or node.parent is None:
            return True
        else:
            return False

    def rbt_tree_try_case2(self, node, sibling):
        if sibling.is_red():
            node.parent.color = "red"
            sibling.color = "black"
            if node is node.parent.left:
                self.rbt_tree_rotate_left(node.parent)
            else:
                self.rbt_tree_rotate_right(node.parent)
            return True
        return False

    def rbt_tree_try_case3(self, node, sibling):
        if node.parent.is_black() and sibling.are_both_children_black():
            sibling.color = "red"
            self.rbt_tree_prepare_for_removal(node.parent)
            return True
        return False

    def rbt_tree_try_case4(self, node, sibling):
        if node.parent.is_red() and sibling.are_both_children_black():
            node.parent.color = "black"
            sibling.color = "red"
            return True
        return False

    def rbt_tree_try_case5(self, node, sibling):
        if self.is_not_none_and_red(sibling.left) and self.is_none_or_black(sibling.right) and node is node.parent.left:
            sibling.color = "red"
            sibling.left.color = "black"
            self.rotate_right(sibling)
            return True
        return False

    def rbt_tree_try_case6(self, node, sibling):
        if self.is_none_or_black(sibling.left) and self.is_not_none_and_red(
                sibling.right) and node is node.parent.right:
            sibling.color = "red"
            sibling.right.color = "black"
            self.rotate_left(sibling)
            return True
        return False

    # def rbt_tree_insert(self,node):
    #     bst_insert(self, node)
    #     node.color = red
    #     rbt_tree_balance(self, node)
    #
    # def rbt_tree_get_uncle(self, node = None):
    #     grandparent = None
    #     if node.parent is not None:
    #         grandparent = node.parent.parent
    #
    #     if grandparent is None:
    #         return None
    #     if grandparent.left == node.parent:
    #         return grandparent.right
    #     else:
    #         return grandparent.left
    #
    #
    # def rbt_tree_balance(self, node = None):
    #     if node.parent is None:
    #         node.color = "black"
    #         return
    #     if node.paren.color == "black":
    #         return
    #     parent = node.parent
    #     grandparent = rbt_tree_get_grandparent(node)
    #     uncle = rbt_tree_get_uncle(node)
    #     if uncle is not None & uncle.color == "red":
    #         parent.color = uncle.color = "black"
    #         grandparent.color = "red"
    #         rbt_tree_balance(self, grandparent)
    #         return
    #     if node == parent.right & parent == grandparent.right:
    #         rbt_tree_rotate_right(self, parent)
    #         node = parent
    #         parent = node.parent
    #
    #     elif node == parent.left & parent == grandparent.left:
    #         rbt_tree_rotate_right(self, parent)
    #         node = parent
    #         parent = node.parent
    #
    #     parent.color = "black"
    #     grandparent.color = "red"
    #     if node == parent.left:
    #         rbt_tree_rotate_right(self, grandparent)
    #     else:
    #         rbt_tree_rotate_left(self, grandparent)
    #
    #
