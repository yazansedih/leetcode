
import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val):
        if val in self.indices:
            return False

        self.indices[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val):
        if val not in self.indices:
            return False

        idx = self.indices[val]
        last_val = self.nums[-1]

        self.nums[idx] = last_val
        self.indices[last_val] = idx

        self.nums.pop()
        del self.indices[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
