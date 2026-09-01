class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        points = []

        for i in range(1, len(nums) - 1):

            if ((nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or
                (nums[i] < nums[i - 1] and nums[i] < nums[i + 1])):

                points.append(i)

        if len(points) < 2:
            return [-1, -1]

        min_dist = float("inf")

        for i in range(len(points) - 1):
            min_dist = min(
                min_dist,
                points[i + 1] - points[i]
            )

        max_dist = points[-1] - points[0]

        return [min_dist, max_dist]