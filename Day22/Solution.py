class Solution:

    def get_height(self, root):
        if not root:
            return -1
        else:
            a = self.get_height(root.left)
            b = self.get_height(root.right)
            if a > b:
                return 1 + a
            else:
                return 1 + b
