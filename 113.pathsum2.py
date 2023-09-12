# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        
        ans = []
        
        def tree_traversal(root, curr_sum, curr_path):
            
            curr_sum += root.val
            curr_path.append(root.val)
            if root.left == None  and root.right == None:
                if curr_sum == targetSum:
                    ans.append(curr_path)
                return
            
            # list() does a deep copy
            if root.left:
                tree_traversal(root.left, curr_sum, list(curr_path))
            
            if root.right:
                tree_traversal(root.right, curr_sum, list(curr_path))
        if root:
            tree_traversal(root, 0, [])
        return ans

if __name__ == "__main__":
    q = TreeNode(5)
    q.left = TreeNode(4)
    q.right = TreeNode(8)
    q.left.left = TreeNode(11)
    q.left.left.left = TreeNode(7)
    q.left.left.right = TreeNode(2)
    
    q.right.left = TreeNode(13)
    q.right.right = TreeNode(4)
    q.right.right.left = TreeNode(5)
    
    
    
    
    
    a = Solution()
    print(a.pathSum(q,22))      
        
