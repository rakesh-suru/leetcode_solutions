class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        def checkCode(c):
            pattern = r"^[A-Za-z0-9_]+$"
            return re.match(pattern, c) is not None
        
        def checkLine(cat):
            valid = ["electronics", "grocery", "pharmacy", "restaurant"]
            return cat in valid
        
        def checkActive(x):
            return x is True
        
        ans = []
        n = len(code)

        for i in range(n):
            if checkCode(code[i]) and checkLine(businessLine[i]) and checkActive(isActive[i]):
                ans.append((businessLine[i], code[i]))

        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        ans.sort(key=lambda x: (order.index(x[0]), x[1]))

        return [c for _, c in ans]
