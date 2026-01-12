class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n-1)) #or use 3 * 2 ** (n-1)
        if k > total:
            return ""

        ans = []
        prev = ''
        for i in range(n):
            for ch in ['a', 'b', 'c']:
                if ch == prev:
                    continue
                count = 1 << (n - i - 1)
                if k > count:
                    k -= count
                else:
                    ans.append(ch)
                    prev = ch
                    break
        return "".join(ans)
