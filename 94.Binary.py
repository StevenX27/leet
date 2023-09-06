# Definition for a binary tree TreeTreeNode.
class TreeTreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeTreeTreeNode
        :rtype: List[int]
        """
        if root is None:
            pass
        else:
            print([root.val])
        return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        # if root is None:
        #     return
 
        # # First recur on left subtree
        # self.inorderTraversal(root.left)
    
        # # Now deal with the TreeTreeNode
        # print(root.val, end=' ')
    
        # # Then recur on right subtree
        # self.inorderTraversal(root.right)

if __name__ == '__main__':
    root = TreeTreeNode(1)
    root.left = TreeTreeNode(None)
    root.right = TreeTreeNode(2)
    root.left.left = TreeTreeNode(3)

 
    # Function call
    print("Inorder traversal of binary tree is:")
    a = Solution()
    a.inorderTraversal(root)