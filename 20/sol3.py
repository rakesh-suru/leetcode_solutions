class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""