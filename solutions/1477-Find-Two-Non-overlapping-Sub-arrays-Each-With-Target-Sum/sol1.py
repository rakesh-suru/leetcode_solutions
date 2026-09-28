class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = float('inf')

        for l1 in range(n):
            for r1 in range(l1, n):

                sum1 = sum(arr[l1:r1 + 1])

                if sum1 != target:
                    continue

                for l2 in range(n):
                    for r2 in range(l2, n):

                        sum2 = sum(arr[l2:r2 + 1])

                        if sum2 != target:
                            continue

                        if r1 < l2 or r2 < l1:
                            length = (r1 - l1 + 1) + (r2 - l2 + 1)
                            ans = min(ans, length)

        return -1 if ans == float('inf') else ans