# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        
        def mark_parents(node, par):
            if not node:
                return
            parent[node] = par
            mark_parents(node.left, node)
            mark_parents(node.right, node)
        
        mark_parents(root, None)
        
        queue = deque([target])
        visited = set([target])
        dist = 0
        
        while queue:
            if dist == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    queue.append(curr.left)
                
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    queue.append(curr.right)
                
                if parent[curr] and parent[curr] not in visited:
                    visited.add(parent[curr])
                    queue.append(parent[curr])
            
            dist += 1
        
        return []