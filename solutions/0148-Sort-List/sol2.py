# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMiddle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow


        def mergeSort(head):
            if not head or not head.next:
                return head
            
            middle = findMiddle(head)
            left = head
            right = middle.next
            middle.next = None

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)
        
        def merge(left, right):
            head = ListNode(-1)
            temp = head

            while left and right:
                if left.val <= right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            
            if left:
                temp.next = left
            else:
                temp.next = right
            
            return head.next

        return mergeSort(head)