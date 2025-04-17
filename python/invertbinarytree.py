class TreeNode:
    def __init__(self, val = 0, left = None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def work(self, root):
        if not root: #we are going to do this using the recursive def so this is not bad
            return None 
        
        #just do the swapping
        root.left, root.right = root.right, root.left

        #call this on the right and left subtrees 
        self.work(root.left)
        self.work(root.right)

        return root
    
def ple(root):
    if not root:
        return []
    results = []
    queue = [root]

    while queue:
        ls = len(queue)

        ln = []

        for i in range(ls):
            node = queue.pop(0)
            ln.append(node.val)
            queue.append(node.left if node.left else None)    
            queue.append(node.right if node.right else None)   

        else:
            ln.append(None)

        while ln and ln[-1] is None:
            ln.pop()

        if ln:
            results.append(ln)

        return results
    
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)

print("Original Tree 1:")
print(ple(root1))

solution = Solution()
inverted1 = solution.work(root1)

print("Inverted Tree 1:")
print(ple(inverted1))
