class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        pos_i, neg_i = 0, 1

        for num in nums:
            if num > 0:
                result[pos_i] = num
                pos_i += 2
            else:
                result[neg_i] = num
                neg_i += 2
        return result
