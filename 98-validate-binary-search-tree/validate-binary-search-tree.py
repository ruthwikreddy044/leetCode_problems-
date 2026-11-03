# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root==None:
            return l
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)

    def isValidBST(self, root: TreeNode | None) -> bool:
        l=[]
        self.inorder(root,l)
        for i in range(len(l)-1):
            if(l[i]>=l[i+1]):
                return False
        return True        
        
        
        