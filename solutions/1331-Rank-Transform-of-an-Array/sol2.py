class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)

        mapper = {}
        rank = 0

        for num in temp:
            if num not in mapper:
                rank += 1
                mapper[num] = rank

        return [mapper[num] for num in arr]