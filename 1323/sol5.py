import re
class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(re.sub('6', '9', str(num), count=1))
