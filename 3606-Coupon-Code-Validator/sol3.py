class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        pattern = re.compile(r"^[A-Za-z0-9_]+$")
        buckets = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": []
        }

        for c, b, a in zip(code, businessLine, isActive):
            if a and b in buckets and pattern.match(c):
                buckets[b].append(c)

        ans = []
        for k in ["electronics", "grocery", "pharmacy", "restaurant"]:
            ans.extend(sorted(buckets[k]))

        return ans
