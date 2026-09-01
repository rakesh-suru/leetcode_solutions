class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        first = -1
        last = -1
        min_dist = float("inf")

        for i in range(1, len(nums) - 1):

            if ((nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or
                (nums[i] < nums[i - 1] and nums[i] < nums[i + 1])):

                if first == -1:
                    first = i
                else:
                    min_dist = min(min_dist, i - last)

                last = i

        if first == last:
            return [-1, -1]

        return [min_dist, last - first]