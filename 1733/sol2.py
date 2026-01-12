from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(l) for l in languages]

        bad_users = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if not lang_sets[u].intersection(lang_sets[v]):
                bad_users.add(u)
                bad_users.add(v)

        if not bad_users:
            return 0

        lang_freq = defaultdict(int)
        for user in bad_users:
            for lang in lang_sets[user]:
                lang_freq[lang] += 1

        max_known = max(lang_freq.values(), default=0)

        return len(bad_users) - max_known
