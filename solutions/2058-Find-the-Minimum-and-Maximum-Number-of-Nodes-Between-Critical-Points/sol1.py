class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        temp = head.next
        cnt = 1
        points = []

        if not head or not head.next or not head.next.next:
            return [-1, -1]

        while temp and temp.next:

            if (temp.val > prev.val and temp.val > temp.next.val) or \
               (temp.val < prev.val and temp.val < temp.next.val):
                points.append(cnt)

            prev = temp
            temp = temp.next
            cnt += 1

        if len(points) < 2:
            return [-1, -1]

        min_dist = float("inf")

        for i in range(len(points) - 1):
            dist = points[i + 1] - points[i]
            min_dist = min(min_dist, dist)

        max_dist = points[-1] - points[0]

        return [min_dist, max_dist]