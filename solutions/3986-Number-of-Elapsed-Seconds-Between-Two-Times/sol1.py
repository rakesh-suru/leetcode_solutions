class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:

        ans = 0
        start = startTime.split(":")
        end = endTime.split(":")

        ans += (int(end[0]) - int(start[0]) % 24) * 60 * 60
        ans += (int(end[1]) - int(start[1]) % 60) * 60
        ans += (int(end[2]) - int(start[2]) % 60)
        
        return ans