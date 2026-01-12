class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        order = []
        top, bottom, left, right = 0, m-1, 0, n-1

        while top <= bottom and left <= right:
            for j in range(left, right+1):
                order.append((top, j))
            top += 1

            for i in range(top, bottom+1):
                order.append((i, right))
            right -= 1

            if top <= bottom:
                for j in range(right, left-1, -1):
                    order.append((bottom, j))
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    order.append((i, left))
                left += 1

        for r, c in order:
            if not head:
                break
            res[r][c] = head.val
            head = head.next

        return res
