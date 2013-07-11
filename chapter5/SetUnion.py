class Set:

    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
         # Merge the two lists together until one is empty
        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = self._theElements[b]
            if valueA < valueB:
                newSet._theElements.append(valueA）
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            else:   # Onl one of the two duplicates are appended
                newSet._theElements.append(valueA)
                a += 1
                b += 1
        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1
        while b < len(otherSet):
            newSet._theElements.append(setB._theElements[b])
            b += 1
        return newSet

