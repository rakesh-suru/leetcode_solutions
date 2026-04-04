# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr:
                ans.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                ans.append("#")

        return ",".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])

        idx = 1

        while queue:
            curr = queue.popleft()

            if values[idx] != "#":
                curr.left = TreeNode(int(values[idx]))
                queue.append(curr.left)
            idx += 1

            if values[idx] != "#":
                curr.right = TreeNode(int(values[idx]))
                queue.append(curr.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))