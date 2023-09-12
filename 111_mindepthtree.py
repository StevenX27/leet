class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self,root):
        # Corner Case.Should never be hit unless the code is
        # called on root = NULL
        if root is None:
            return 0
        
        # Base Case : Leaf node.This accounts for height = 1
        if root.left is None and root.right is None:
            return 1
        
        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.minDepth(root.right)+1
        
        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.minDepth(root.left) +1
        
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
        
if __name__ == "__main__":
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left.left = TreeNode(4)
    
    a = Solution()
    print(a.minDepth(q))      
        
