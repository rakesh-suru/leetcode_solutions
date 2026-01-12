class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = []
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                ones.append(i)

        for one in ones:
            left = (one - k) if (one - k) > 0 else 0
            right = (one + k + 1) if (one + k + 1) < n else n
            temp = nums[left:right]

            if temp.count(1) > 1:
                return False

        return True
