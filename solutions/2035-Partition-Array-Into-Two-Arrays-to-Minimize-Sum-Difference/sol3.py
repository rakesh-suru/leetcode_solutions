class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums) // 2

        left = nums[:n]
        right = nums[n:]

        left_sums = defaultdict(list)
        right_sums = defaultdict(list)

        def generate(arr, idx, count, curr_sum, store):

            if idx == len(arr):
                store[count].append(curr_sum)
                return

            generate(
                arr,
                idx + 1,
                count + 1,
                curr_sum + arr[idx],
                store
            )

            generate(
                arr,
                idx + 1,
                count,
                curr_sum,
                store
            )

        generate(left, 0, 0, 0, left_sums)
        generate(right, 0, 0, 0, right_sums)

        total = sum(nums)
        target = total // 2

        for k in right_sums:
            right_sums[k].sort()

        ans = float("inf")

        for left_count in left_sums:

            right_count = n - left_count

            r = right_sums[right_count]

            for s1 in left_sums[left_count]:

                need = target - s1

                idx = bisect_left(r, need)

                for j in [idx - 1, idx]:

                    if 0 <= j < len(r):

                        curr = s1 + r[j]

                        other = total - curr

                        ans = min(ans, abs(curr - other))

        return ans