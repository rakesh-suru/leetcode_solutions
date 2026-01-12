class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        left = set()
        right = Counter(s)

        for mid in s:
            right[mid] -= 1
            for c in left:
                if right[c] > 0:
                    ans.add((mid, c))
            left.add(mid)
        return len(ans)
