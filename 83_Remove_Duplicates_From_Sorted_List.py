"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    #def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        while currentNode and currentNode.next:
            if currentNode.next.val == currentNode.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
                
        return head
            
        
if __name__ == '__main__':
    print(Solution.deleteDuplicates([1,1,2]))