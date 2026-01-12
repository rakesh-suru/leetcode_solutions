class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        for i in range(2 ** n):
            bin_str = format(i, f'0{n}b')
            if "00" not in bin_str:
                res.append(bin_str)
        return res
