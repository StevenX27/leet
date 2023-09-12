# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        sum = 0
        
        def pathsum(root,sum):
            # Corner Case.Should never be hit unless the code is
            # called on root = NULL
            if root is None:
                return False
            if root.left is None and root.right is None:
                sum += root.val
                if sum == targetSum:
                    return True
            
            left = pathsum(root.left,sum+root.val)
            right = pathsum(root.right,sum+root.val)
            
            return left or right
            
        return pathsum(root,sum)    


if __name__ == "__main__":
    q = TreeNode(5)
    q.left = TreeNode(4)
    q.right = TreeNode(8)
    q.left.left = TreeNode(11)
    q.left.left.left = TreeNode(7)
    q.left.left.right = TreeNode(2)
    
    q.right.left = TreeNode(13)
    
    
    
    a = Solution()
    print(a.hasPathSum(q,22))      
        
