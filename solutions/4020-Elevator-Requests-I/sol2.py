class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        if not requests:
            return 0

        ans = requests[0]

        for i in range(len(requests) - 1):
            ans += abs(requests[i] - requests[i + 1])

        return ans