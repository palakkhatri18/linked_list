# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        

class Solution:
    #Function to check whether two linked lists are identical or not.
    def areIdentical(self, head1, head2):
        # Code
        a=[]
        b=[]
        
        while head1:
            a.append(head1.data)
            head1=head1.next
        
        while head2:
            b.append(head2.data)
            head2=head2.next
        return a==b 