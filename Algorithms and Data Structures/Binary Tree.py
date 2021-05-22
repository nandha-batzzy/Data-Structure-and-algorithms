class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_tree(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.add_tree(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                return self.right.add_tree(data)
            else:
                self.right = BinaryTree(data)

    def inorderTree(self):
        element = []
        if self.left:
            element = element + self.left.inorderTree()

        element.append(self.data)

        if self.right:
            element = element + self.right.inorderTree()

        return element

    def searchtree(self, val):
        if self.data == val:
            return val

        if val < self.data:
            if self.left:
                return self.left.searchtree(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.searchtree(val)
            else:
                return False

    def mini(self):
        if self.left is None:
            return self.data
        else:
            return self.left.mini()

    def maxx(self):
        if self.right is None:
            return self.data
        else:
            return self.right.maxx()

    def summ(self):
        m = 0
        if self.left:
            m = m + self.left.summ()
        m = m + self.data
        if self.right:
            m = m + self.right.summ()
        return m

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements


def buid_tree(element):
    root = BinaryTree(element[0])
    for i in range(1, len(element)):
        root.add_tree(element[i])

    return root


if __name__ == '__main__':
    num = [7, 12, 14, 15, 20, 23, 27, 28]
    tree = buid_tree(num)
    print(tree.post_order_traversal())
    print(tree.searchtree(6))
    print(tree.mini())
    print(tree.summ())
