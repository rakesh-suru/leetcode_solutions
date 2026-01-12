class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')
        l1, l2 = len(list1), len(list2)
        if l1 != l2:
            if l1 > l2:
                for i in range(abs(l1-l2)):
                    list2.append('0')
            else:
                for i in range(abs(l1-l2)):
                    list1.append('0')
        for i in range(max(l1,l2)):
            if int(list1[i].lstrip("0") or "0") > int(list2[i].lstrip("0") or "0"):
                return 1
            elif int(list1[i].lstrip("0") or "0") < int(list2[i].lstrip("0") or "0"):
                return -1
            else:
                continue
        return 0




        