import re

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pattern = re.compile(f'^{re.escape(pref)}')
        return sum(1 for word in words if pattern.match(word))
