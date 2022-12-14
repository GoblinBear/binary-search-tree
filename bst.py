class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if value > current.data:
                if current.right is None:
                    current.right = Node(value)
                    return

                current = current.right
            else:
                if current.left is None:
                    current.left = Node(value)
                    return

                current = current.left

    def search(self, value):
        current = self.root
        while current:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else:
                return current

        return None

    def get_top_k(self, k):
        stack = []
        current = self.root
        count = 0
        result = []

        while (stack or current) and count < k:
            if current:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                result.append(current.data)
                count = count + 1
                current = current.left

        return result

    def delete(self, value):
        current = self.root
        current_parent = None

        while current and current.data != value:
            current_parent = current
            if value < current.data:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        if current.left and current.right:
            min_current = current.right
            min_current_parent = current
            while min_current.left:
                min_current_parent = min_current
                min_current = min_current.left

            current.data = min_current.data
            current = min_current
            current_parent = min_current_parent

        child = None
        if current.left:
            child = current.left
        elif current.right:
            child = current.right
        else:
            child = None

        if current_parent is None:
            self.root = child
        elif current_parent.left is current:
            current_parent.left = child
        else:
            current_parent.right = child

        return True

    def __depth(self, root):
        if root is None:
            return 0

        left_depth = self.__depth(root.left)
        right_depth = self.__depth(root.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def inorder_traversal_ascending(self):
        stack = []
        current = self.root
        result = []

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.data)
                current = current.right

        return result

    def inorder_traversal_descending(self):
        stack = []
        current = self.root
        result = []

        while stack or current:
            if current:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                result.append(current.data)
                current = current.left

        return result

    def display(self):
        print()
        picture = []

        depth = self.__depth(self.root)

        picture.append([self.root])
        for i in range(depth - 1):
            raw = []
            for node in picture[-1]:
                if node.data is None:
                    raw.append(Node(None))
                    raw.append(Node(None))
                else:
                    if node.left is None:
                        raw.append(Node(None))
                    else:
                        raw.append(node.left)

                    if node.right is None:
                        raw.append(Node(None))
                    else:
                        raw.append(node.right)

            picture.append(raw)

        for i, raw in enumerate(picture):
            h = depth - i

            pre_space = 2
            interval_space = 2
            for i in range(1, h):
                pre_space = pre_space + pow(2, i)
                interval_space = interval_space + pow(2, i + 1)

            for i in range(pre_space):
                print(' ', end='')

            for item in raw:
                if item.data:
                    # print(f'00', end='')
                    print(f'{item.data:2d}', end='')
                else:
                    # print(f'XX', end='')
                    print(f'--', end='')

                for i in range(interval_space):
                    print(' ', end='')

            print('\n')


def main():
    bst = BST()
    bst.insert(24)
    bst.insert(28)
    bst.insert(26)
    bst.insert(27)
    bst.insert(25)
    bst.insert(12)
    bst.insert(18)
    bst.insert(15)
    bst.insert(20)
    bst.insert(35)
    bst.insert(42)
    bst.insert(40)
    bst.insert(33)
    bst.insert(30)
    bst.insert(34)
    bst.insert(49)

    bst.display()
    print(bst.inorder_traversal_ascending())
    print(bst.inorder_traversal_descending())
    print(bst.get_top_k(3))
    print(bst.get_top_k(5))


if __name__ == '__main__':
    main()
