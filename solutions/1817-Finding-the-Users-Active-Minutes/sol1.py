class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        mapper = defaultdict(set)

        for user, time in logs:
            mapper[user].add(time)

        ans = [0] * k

        for user in mapper:
            uam = len(mapper[user])
            if uam <= k:
                ans[uam - 1] += 1

        return ans