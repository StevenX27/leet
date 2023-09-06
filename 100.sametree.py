# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False   
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        
        
    def inorder(self,root,order):
        
        if root is None:
            return
        
        # First recur on left subtree
        self.inorder(root.left,order)
        order.append(root.val)
       
        # Now deal with the TreeTreeNode
    
        # Then recur on right subtree
        self.inorder(root.right,order)
        
if __name__ == "__main__":
    q = TreeNode(1)
    q.left = TreeNode(1)
    # q.right = TreeNode(3)
    
    p = TreeNode(1)
    p.left = TreeNode(None)
    p.right = TreeNode(1)
    a = Solution()
    a.isSameTree(q,p)