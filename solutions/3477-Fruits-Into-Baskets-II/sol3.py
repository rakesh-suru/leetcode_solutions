class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        vis = [False] * n
        ans = n
        for x in fruits:
            for i, cap in enumerate(baskets):
                if not vis[i] and cap >= x:
                    vis[i] = True
                    ans -= 1
                    break
        return ans
