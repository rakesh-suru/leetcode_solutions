class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        pattern = re.compile(r"^[A-Za-z0-9_]+$")
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        valid = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in order and pattern.match(code[i]):
                valid.append((order[businessLine[i]], code[i]))

        valid.sort()
        return [c for _, c in valid]
