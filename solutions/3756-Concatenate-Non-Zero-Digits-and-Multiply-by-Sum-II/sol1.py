class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        ans = []

        def solve(val):
            digit_sum = sum(int(ch) for ch in val)

            new_num = 0
            for ch in val:
                if ch != '0':
                    new_num = new_num * 10 + int(ch)

            return (new_num * digit_sum) % MOD
        
        for l, r in queries:
            ans.append(solve(s[l:r+1]))
        
        return ans