class ExpressionTree:
    # Builds an expression tree for the expression string.
    def __inti__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)

    # Evaluates the expression tree and returns the resulting value.
    def evaluate(self, varMap):
        return self._evalTree(self._expTree, varMap)
    
    # Returns a tring representation of the expression tree.
    def __str__(self):
        return self._buildString(self._expTree)

    
    # Sorage class for creating the tree nodes.
class _ExpTreeNode:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None


