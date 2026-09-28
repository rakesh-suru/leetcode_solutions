class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                temp = 0

                for i in range(n):
                    for j in range(n):
                        ni = i + dx
                        nj = j + dy

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                temp += 1

                ans = max(ans, temp)

        return ans