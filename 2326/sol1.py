class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while head and top <= bottom and left <= right:

            for col in range(left, right + 1):
                if not head:
                    return mat
                mat[top][col] = head.val
                head = head.next
            top += 1

            for row in range(top, bottom + 1):
                if not head:
                    return mat
                mat[row][right] = head.val
                head = head.next
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if not head:
                        return mat
                    mat[bottom][col] = head.val
                    head = head.next
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if not head:
                        return mat
                    mat[row][left] = head.val
                    head = head.next
                left += 1

        return mat