class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        left = [0] * n
        right = [0] * n

        curr = 1
        left[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                curr += 1
            else:
                curr = 1
            left[i] = curr

        curr = 1
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr += 1
            else:
                curr = 1
            right[i] = curr

        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])
        
        return ans