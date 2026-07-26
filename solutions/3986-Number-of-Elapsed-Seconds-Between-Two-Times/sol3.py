class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh, sm, ss = map(int, startTime.split(":"))
        eh, em, es = map(int, endTime.split(":"))

        ans = (eh - sh) * 3600 + (em - sm) * 60 + (es - ss)
        return ans % (24 * 3600)