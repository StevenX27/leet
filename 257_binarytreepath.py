class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_path = []
        
        def tree_traversal(root, curr_path):
            
            if curr_path =="":
                curr_path += str(root.val)
            else:
                
                curr_path += "->" + str(root.val)

            if root.left == None  and root.right == None:
                all_path.append(curr_path)
                return
            
            # list() does a deep copy
            if root.left:
                tree_traversal(root.left, curr_path)
            
            if root.right:
                tree_traversal(root.right, curr_path)
        
        tree_traversal(root,"")
        return print(all_path)

if __name__ == "__main__":
    q = TreeNode(5)
    q.left = TreeNode(4)
    q.right = TreeNode(8)
    q.left.left = TreeNode(11)
    q.left.left.left = TreeNode(7)
    q.left.left.right = TreeNode(2)
    a = Solution()
    a.binaryTreePaths(q)