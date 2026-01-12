import re

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not re.match(r'^[a-zA-Z0-9]+$', word):
            return False
        if not re.search(r'[aeiouAEIOU]', word):
            return False
        if not re.search(r'[^aeiouAEIOU0-9]', word):
            return False
        return True
