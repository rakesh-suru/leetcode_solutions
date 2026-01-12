class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cols = [chr(c) for c in range(ord(s[0]), ord(s[3])+1)]
        rows = [str(r) for r in range(int(s[1]), int(s[4])+1)]
        return [c + r for c, r in product(cols, rows)]
