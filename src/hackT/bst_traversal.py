""" Day 23: BST Level-Order Traversal """
class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrderInt(self, root, queue, result):
        """ Internal call of levelOrder with more parameters to collect output.

            Args:            
                queue (list): Temp queue for creating output
                result (list): List of Node.data values in BST level order

            Returns:
                levelOrderInt: None
        """
        result.append(root.data)

        if root.left is not None:
            queue.append(root.left)

        if root.right is not None:
            queue.append(root.right)


    def levelOrder(self, root):
        """ Returns list of data in BST Level-Order Traversal """
        queue = [root]
        result = []

        while len(queue) > 0:            
            self.levelOrderInt(queue.pop(0), queue, result)

        return result
    


