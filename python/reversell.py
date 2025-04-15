class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def work(self, head):
        cur = head
        prev = None
        next = None

        while cur:
            next = cur.next #so we are to think of this as a pointer to the next element that is in our list
            cur.next = prev
            prev = cur
            cur = next

        return prev
    



# Function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    
    for val in values:
        current.next = ListNode(val)
        current = current.next
        
    return dummy.next

# Function to print a linked list
def print_linked_list(head):
    values = []
    current = head
    
    while current:
        values.append(str(current.val))
        current = current.next
        
    print(" -> ".join(values))

# Test the solution
if __name__ == "__main__":
    # Create a test linked list: 1 -> 2 -> 3 -> 4 -> 5
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    
    print("Original linked list:")
    print_linked_list(head)
    
    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.work(head)
    
    print("Reversed linked list:")
    print_linked_list(reversed_head)