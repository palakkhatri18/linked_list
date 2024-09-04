class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def sortedInsert(self, head, x):
        # code here
        # return head of edited linked list
        new_node = ListNode(x)
        
        # If the linked list is empty or the new node should be inserted at the head
        if not head or x <= head.data:
            new_node.next = head
            return new_node

        # Traverse the list to find the correct position to insert the new node
        current = head
        while current.next and current.next.data < x:
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

        return head