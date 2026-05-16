class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        min_time = 0
        max_time = 0

        for actual, minimum in tasks:
            min_time += actual
            max_time += minimum

        tasks.sort(key=lambda x: -(x[1] - x[0]))

        for energy in range(min_time, max_time + 1):

            temp = energy
            completed = True

            for actual, minimum in tasks:

                if temp < minimum:
                    completed = False
                    break

                temp -= actual

            if completed:
                return energy

        return -1