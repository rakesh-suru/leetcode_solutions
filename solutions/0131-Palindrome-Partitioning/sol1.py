class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def solve(index, store):
            if index == n:
                ans.append(store[:])
                return 

            for i in range(index, n):
                temp = s[index : i + 1]
                if  temp == temp[::-1]:
                    store.append(temp)
                    solve(i + 1, store)
                    store.pop()
        
        solve(0, [])
        return ans
