class ExpressionTree:
    
    # Recursively builds a strig representation of the expression tree.
    def _buildString(self, treeNode):
        # If the node is a leaf, it's an operand
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)
        else:
            expStr = '('
            expStr += self._buildString(treeNode.left)
            expStr += str(treeNode.element)
            expStr += self._buildString(treeNode.right)
            expStr +=')'
            return expStr

