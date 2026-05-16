class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return

            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        mapper = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]

                if mail not in mapper:
                    mapper[mail] = i
                else:
                    union(i, mapper[mail])

        merged = defaultdict(list)

        for mail, idx in mapper.items():
            node = find(idx)
            merged[node].append(mail)

        ans = []

        for node, mails in merged.items():
            temp = [accounts[node][0]]
            temp.extend(sorted(mails))
            ans.append(temp)

        return ans