# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def findorder(root):
            
            if root is None:
                return
            
            findorder(root.left)
            findorder(root.right)
            self.count += 1
           
        findorder(root)
        print(self.count)
        return self.count


if __name__ == "__main__":
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left.left = TreeNode(4)
    
    a = Solution()
    a.countNodes(q)    