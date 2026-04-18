class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n

        while temp:
            rem = temp % 10
            rev = rev * 10 + rem
            temp = temp // 10

        return abs(n - rev)