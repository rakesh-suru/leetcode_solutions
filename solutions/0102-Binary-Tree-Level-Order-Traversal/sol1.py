class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            level_size = len(queue)
            temp = []
            
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(temp)
        
        return ans