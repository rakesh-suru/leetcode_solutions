class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for n1, n2 in zip_longest(version1.split("."), version2.split("."), fillvalue="0"):
            if int(n1) < int(n2):
                return -1
            elif int(n1) > int(n2):
                return 1
        return 0
