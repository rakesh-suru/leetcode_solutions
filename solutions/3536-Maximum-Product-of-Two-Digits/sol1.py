class Solution:
    def maxProduct(self, n: int) -> int:
        temp = [int(i) for i in str(n)]
        temp.sort(reverse = True)
        return temp[0] * temp[1]