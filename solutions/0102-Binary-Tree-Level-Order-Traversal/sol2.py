class Solution:
    def levelOrder(self, root):
        ans = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level == len(ans):
                ans.append([])
            
            ans[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return ans