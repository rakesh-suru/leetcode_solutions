class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        def canFinish(energy):

            curr = energy
            for actual, minimum in tasks:
                if curr < minimum:
                    return False
                curr -= actual
            return True

        left = sum(x[0] for x in tasks)
        right = sum(x[1] for x in tasks)

        while left <= right:

            mid = (left + right) // 2

            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left