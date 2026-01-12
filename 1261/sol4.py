class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0

        def recover(node):
            if not node:
                return
            if node.left:
                node.left.val = 2 * node.val + 1
                recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                recover(node.right)
        
        recover(self.root)

    def find(self, target: int) -> bool:
        path = []
        while target > 0:
            parent = (target - 1) // 2
            path.append(target % 2)  # 1 if left, 0 if right (reverse)
            target = parent

        node = self.root
        for direction in reversed(path):
            if direction == 1:
                if not node.left:
                    return False
                node = node.left
            else:
                if not node.right:
                    return False
                node = node.right
        return True
