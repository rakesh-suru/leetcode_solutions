class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        for i in range(len(hours)):
            if hours[i] >= target:
                hours[i] = -1
        return hours.count(-1)