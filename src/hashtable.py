# '''
# Linked List hash table key/value pair
# '''
import warnings

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        current_pair = self.storage[self._hash_mod(key)]
        if current_pair:
            while True:
                if current_pair.key == key:
                    current_pair.value = value
                    break
                else:
                    if current_pair.next:
                        current_pair = current_pair.next
                    else:
                        current_pair.next = LinkedPair(key, value)
                        break
        else:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        current_pair = self.storage[self._hash_mod(key)]
        if current_pair:
            if current_pair.key == key:
                self.storage[self._hash_mod(key)] = current_pair.next
            else:
                while True:
                    if current_pair.next.key == key:
                        current_pair.next = current_pair.next.next
                        break
                    else:
                        if current_pair.next.next:
                            current_pair = current_pair.next
                        else:
                            warnings.warn("Key not found!")
                            break
        else:
            warnings.warn("Key not found!")



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        current_pair = self.storage[self._hash_mod(key)]
        if current_pair:
            while True:
                if current_pair.key == key:
                    return current_pair.value
                else:
                    if current_pair.next:
                        current_pair = current_pair.next
                    else:
                        return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.__init__(self.capacity * 2)
        for pair in old_storage:
            if pair:
                current_pair = pair
                while current_pair:
                    self.insert(current_pair.key, current_pair.value)
                    current_pair = current_pair.next




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
