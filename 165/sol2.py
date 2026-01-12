class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = l2 = 0
        r1 = r2 = 0
        n1, n2 = len(version1), len(version2)

        while l1 < n1 or l2 < n2:
            r1 = l1
            while r1 < n1 and version1[r1] != '.':
                r1 += 1

            r2 = l2
            while r2 < n2 and version2[r2] != '.':
                r2 += 1
            
            num1 = int(version1[l1:r1]) if l1 < n1 else 0
            num2 = int(version2[l2:r2]) if l2 < n2 else 0

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

            l1 = r1 + 1
            l2 = r2 + 1

        return 0
