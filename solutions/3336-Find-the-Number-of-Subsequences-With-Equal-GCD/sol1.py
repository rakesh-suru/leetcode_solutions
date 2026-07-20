class Solution:
    def subsequencePairCount(self, nums: List[int]) ->int:
        n = len(nums)

        def find_gcd(arr):
            if not arr:
                return 0

            g = arr[0]
            for x in arr[1:]:
                g = math.gcd(g, x)
            return g

        def solve(i, seq1, seq2):
            if i == n:
                if not seq1 or not seq2:
                    return 0
                return 1 if find_gcd(seq1) == find_gcd(seq2) else 0

            ans = solve(i + 1, seq1, seq2)

            seq1.append(nums[i])
            ans += solve(i + 1, seq1, seq2)
            seq1.pop()

            seq2.append(nums[i])
            ans += solve(i + 1, seq1, seq2)
            seq2.pop()

            return ans

        return solve(0, [], [])