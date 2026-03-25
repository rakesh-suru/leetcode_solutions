class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mapper = {}
        ans = [0] * k

        for user, time in logs:
            if user not in mapper:
                mapper[user] = set()
            mapper[user].add(time)

        for user in mapper:
            uam = len(mapper[user])
            if uam <= k:
                ans[uam - 1] += 1

        return ans