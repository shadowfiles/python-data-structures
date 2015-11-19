from copy import deepcopy

class hashtable:
    STARTING_SIZE = 10
    MAX_LOAD_FACTOR = 0.70

    def __init__(self):
        self.table = [None] * self.STARTING_SIZE
        self.size = 0

    def add(self, key, value):
        self.__resize()

        i = self.__hash_index(key)
        if i == None:
            self.table[i] = self.entry(key, value)
        else:
            last = None
            curr = self.table[i]
            while not curr is None:
                if curr.key == key:
                    old = curr.value
                    curr.value = value
                    return old
                last = curr
                curr = curr.next
            if last is None:
                self.table[i] = self.entry(key, value)
            else:
                last.next = self.entry(key, value)

        self.size += 1
        return None

    def get(self, key):
        i = self.__hash_index(key)
        entry = self.table[i]
        while not entry is None:
            if entry.key == key:
                return entry.value
            entry = entry.next

        return None

    def remove(self, key):
        i = self.__hash_index(key)
        if self.table[i].key == key:
            value = self.table[i].value
            self.table[i] = self.table[i].next
            self.size -= 1
            return value
        elif not self.table[i] is None:
            if self.table[i].key == key:
                value = self.table[i].value
                self.table[i] = self.table[i].next
                self.size -= 1
                return value
            last = self.table[i]
            curr = self.table[i].next
            while not curr is None:
                if curr.key == key:
                    value = curr.value
                    last.next = curr.next
                    self.size -= 1
                    return value
                last = curr
                curr = curr.next
        return None

    def key_set(self):
        result = []
        for entry in self.table:
            while not entry is None:
                result.append(entry.key)
                entry = entry.next
        return result

    def __resize(self):
        if self.size > len(self.table) * self.MAX_LOAD_FACTOR:
            old_table = self.table
            self.table = [None] * len(old_table) * 2
            self.size = 0
            for entry in old_table:
                while not entry is None:
                    self.add(entry.key, entry.value)
                    entry = entry.next

    def __hash_index(self, obj):
        if obj.__hash__ is None:
            raise NotImplementedError("Object is not hashable")
        return abs(obj.__hash__()) % len(self.table)

    def __add__(self, other):
        result = deepcopy(self)
        for entry in other:
            result.add(entry, other.get(entry))
        return result

    def __str__(self):
        result = ""
        for entry in self.table:
            while not entry is None:
                result += "{} => {}, ".format(str(entry.key), str(entry.value))
                entry = entry.next
        return result

    def __iter__(self):
        for entry in self.table:
            while not entry is None:
                yield entry.key
                entry = entry.next

    class entry:
        key = None
        value = None
        next = None

        def __init__(self, k, v, n = None):
            self.key = k
            self.value = v
            self.next = n
