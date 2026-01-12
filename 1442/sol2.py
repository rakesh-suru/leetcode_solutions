class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            xor = 0
            for k in range(i, n):
                xor ^= arr[k]
                if xor == 0 and k > i:
                    ans += k - i
        return ans
