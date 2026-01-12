class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = [row.count("1") for row in bank if "1" in row]
        return sum(a * b for a, b in zip(temp, temp[1:]))