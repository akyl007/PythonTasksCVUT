class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.visits = 0

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            return

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def fromArray(self, array):
        for i in array:
            self.insert(i)
        return

    def _search(self, value, cur_node):
        if value == cur_node.value:
            self.count +=1;
            return True
        elif value < cur_node.value and cur_node.left is not None:
            self.count += 1
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            self.count +=1
            return self._search(value, cur_node.right)
        else:
            self.count += 1
            return False

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)

        return False

    def _min(self, cur_node):
        if cur_node.left is not None:
            self.count += 1
            return self._min(cur_node.left)
        elif cur_node.left is None:
            self.count += 1
            return cur_node.value
        else:
            return False

    def min(self):
        if self.root is not None:
            return self._min(self.root)

    def _max(self, cur_node):
        if cur_node.right is not None:
            self.count += 1
            return self._max(cur_node.right)
        elif cur_node.right is None:
            self.count += 1
            return cur_node.value
        else:
            return False

    def max(self):
        if self.root is not None:
            return self._max(self.root)

    def visitedNodes(self):
        tmp = self.count
        self.count = 0
        return tmp

    def inOrder_print(self, cur_node):
        if cur_node is not None:
            self.inOrder_print(cur_node.left)
            print(str(cur_node.value))
            self.inOrder_print(cur_node.right)

    def print(self):
        if self.root is not None:
            self.inOrder_print(self.root)

