class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        size = n + forget + 5
        add = [0] * size
        rem = [0] * size
        add[1 + delay] = 1
        rem[1 + forget] = 1
        active_sharers = 0
        total = 1
        for day in range(2, n + 1):
            if rem[day]:
                total = (total - rem[day]) % MOD
                active_sharers -= rem[day]
            if add[day]:
                active_sharers += add[day]
            new_people = active_sharers % MOD
            total = (total + new_people) % MOD
            if new_people:
                add[day + delay] = (add[day + delay] + new_people) % MOD
                rem[day + forget] = (rem[day + forget] + new_people) % MOD
        return total % MOD
