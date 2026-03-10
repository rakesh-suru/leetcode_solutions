class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def find(temp, k):
            for _ in range(k - 1):
                if not temp:
                    return None
                temp = temp.next
            return temp

        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        temp = head
        prevLast = None

        while temp:
            kth_node = find(temp, k)

            if not kth_node:
                if prevLast:
                    prevLast.next = temp
                break

            next_node = kth_node.next
            kth_node.next = None

            newHead = reverse(temp)

            if temp == head:
                head = newHead
            else:
                prevLast.next = newHead

            prevLast = temp
            temp = next_node

        return head