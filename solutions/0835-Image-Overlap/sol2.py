class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):

                temp = 0

                for i in range(n):
                    ni = i + dx

                    if not (0 <= ni < n):
                        continue

                    for j in range(n):
                        nj = j + dy

                        if 0 <= nj < n:
                            temp += img1[i][j] & img2[ni][nj]

                ans = max(ans, temp)

        return ans