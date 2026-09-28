class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        n = len(nums1)

        possible = []

        for i in range(n):
            parities = {nums1[i] % 2}

            for j in range(n):
                if i != j:
                    parities.add((nums1[i] - nums1[j]) % 2)

            possible.append(parities)

        all_even = all(0 in p for p in possible)

        all_odd = all(1 in p for p in possible)

        return all_even or all_odd