from hashmap import HashMap

class Histogram:
    # Create a histogram containing the given categories
    def __init__(self, catSeq):
        self._freqCounts = HashMap()
        for cat in catSeq:
            self._freqCounts.add(cat, 0)

    def getCount(self, category):
        assert category in self._freqCounts, "Invalid histogram category."
        return self._freqCounts.valueOf(category)
    
    # Increments the counter for the given category.
    def incCount(self, category):
        assert category in self._freqCounts, "Invalid histogram category."
        value = self._freqCounts.valueOf(category)
        self._freqCounts.add(category, value+1)

    # Returns the sum of the frequency counts.
    def totalCount(self):
        total = 0
        for cat in self._freqCounts:
            total += self._freqCounts.valueOf(cat)
        return total
     
    # Returns an iterator for traversing the categories.
    def __iter__(self):
        return iter(self._freqCounts)

