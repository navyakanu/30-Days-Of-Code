class Solution:

    def __init__(self):
        self.maximum_difference = 0

    def compute_difference(self):
        for a in self.__elements:
            for b in self.__elements:
                if abs(a - b) > self.maximum_difference:
                    self.maximumDifference = abs(a - b)


