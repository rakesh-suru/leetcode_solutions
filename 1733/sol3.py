from typing import List
from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_lang = [set(l) for l in languages]

        bad_users = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if user_lang[u].isdisjoint(user_lang[v]):
                bad_users.add(u)
                bad_users.add(v)

        if not bad_users:
            return 0

        lang_count = Counter()
        for u in bad_users:
            lang_count.update(user_lang[u])

        return len(bad_users) - max(lang_count.values())
