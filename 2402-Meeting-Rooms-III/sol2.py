class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end_time = [0] * n
        count = [0] * n

        for start, end in meetings:
            chosen = -1
            for i in range(n):
                if end_time[i] <= start:
                    chosen = i
                    break

            if chosen == -1:
                chosen = min(range(n), key=lambda i: end_time[i])
                end = end_time[chosen] + (end - start)

            end_time[chosen] = end
            count[chosen] += 1

        return count.index(max(count))