class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def work(self, list1, list2):

        if not list1:
            return list2
        if not list2:
            return list1
        
        #find the head that we want to start with
        dummy = ListNode(0)
        cur = dummy

        # if list1.val > list2.val: #we cant have this because it skips a value
        #     dummy.next = list2
        #     #may need to move the pointer over 
        #     list2 = list2.next
        # else:
        #     dummy.next = list1
        #     list1 = list1.next

        #now we are going to go from on to the other looking to see whats up 
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
            
        #check if there is anything else left 
        if list1:
            cur.next = list1

        else:
            cur.next = list2
        return dummy.next
    
def creatll(val):
    head = ListNode(0)
    cur = head

    for v in val:
        cur.next = ListNode(v)
        cur = cur.next

    return head.next

def printll(head):
    values = []
    cur = head 

    while cur:
        values.append(str(cur.val))
        cur = cur.next 
    
    print("->".join(values))

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,5]

    ll1 = creatll(list1)
    ll2 = creatll(list2)
    printll(ll1)
    printll(ll2)

    solution = Solution()
    merged = solution.work(ll1, ll2)
    printll(merged)

