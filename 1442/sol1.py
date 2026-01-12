class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                a = 0
                for x in range(i, j):
                    a ^= arr[x]
                b = 0
                for y in range(j, n):
                    b ^= arr[y]
                    if a == b:
                        ans += 1
        return ans