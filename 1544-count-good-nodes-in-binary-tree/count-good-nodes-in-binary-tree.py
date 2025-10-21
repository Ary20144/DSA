# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        goodnodes = []
        value=root.val
        maxval=-1000000
        self.dfs(root,goodnodes,value,maxval)
        print(goodnodes)
        if len(goodnodes)==0:
            return 1
        else:
            return len(goodnodes)
    def dfs(self, root, result,value,max):
        if not root:
            return
        else:
            if (root.val>=value) and (root.val>=max):
                max=root.val
                result.append(root.val)
        self.dfs(root.right,result,root.val,max)
        self.dfs(root.left,result,root.val,max)
        
