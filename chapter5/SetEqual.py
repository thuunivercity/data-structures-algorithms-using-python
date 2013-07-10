class Set:
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True
