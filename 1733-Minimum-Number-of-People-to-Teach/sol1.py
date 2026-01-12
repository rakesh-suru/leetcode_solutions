from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(l) for l in languages]

        bad_users = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if lang_sets[u].intersection(lang_sets[v]):  
                continue
            bad_users.add(u)
            bad_users.add(v)

        if not bad_users:
            return 0

        res = float("inf")
        for lang in range(1, n+1):
            teach_count = 0
            for user in bad_users:
                if lang not in lang_sets[user]:
                    teach_count += 1
            res = min(res, teach_count)

        return res
