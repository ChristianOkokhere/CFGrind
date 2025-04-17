class ListNode:

    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def work(self, head):
        #we need some sort of check 
        if not head or not head.next: #we are checking this here because we need at least two nodes to make this work
            return None
        
        slow = head #these are the things that we are looking at here 
        fast = head #we can set both to be at the begining of the list

        #this algo is split into two parts here
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if fast == slow:
                #slow = head we are going back to the begin of the ll
                #while slow != fast:
                    #slow = slow.next
                    #fast = fast.next 
                #return slow 
        
                
                
                return False
        return True
    

def creatll(values):
    dummy = ListNode(0)
    cur = dummy 

    for val in values:
        cur.next = ListNode(val)
        cur = cur.next

    return dummy.next

def printll(head):
    values = []
    cur = head

    while cur:
        values.append(str(cur.val))
        cur = cur.next

    print(" -> ".join(values))

if __name__ == '__main__':

    val = [3,2,4,0,-4, 2]
    head = creatll(val)

    printll(head)
    solution = Solution()
    cycc = solution.work(head)
    print(cycc)