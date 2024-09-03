class Solution:
    def isCircular(self, head):
        # Code here
        head=temp
        while temp.next==head:
            
            temp=temp.next
            
            return True
        return False