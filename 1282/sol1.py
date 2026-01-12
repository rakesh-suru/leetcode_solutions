class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        groups = defaultdict(list)

        for i, size in enumerate(groupSizes):
            groups[size].append(i)

            if len(groups[size]) == size:
                ans.append(groups.pop(size))
        return ans