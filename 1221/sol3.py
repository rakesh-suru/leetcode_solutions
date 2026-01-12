class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = r_count = count = 0
        for char in s:
            if char == 'L':
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                count += 1
        return count
