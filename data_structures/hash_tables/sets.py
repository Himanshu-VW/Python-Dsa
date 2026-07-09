# set have O(1) search time because python by itself implements hash function for immutables
'''
Hash function is with which value passes before put into a hashtable. It converts the object in to unique int(hash value)
which decides it's location in memory
'''
# sets are unique and sorted
set = {1,2,3} # defining set
# list to set
list = [1,2,4,3,5,4]
my_set = set(list)

#you have to implement you own hash function using __hash__ for custom classes objects(below example)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # 1. Tell Python how to compare two books
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # 2. Tell Python how to hash the book
    def __hash__(self):
        # We leverage Python's built-in string hashing!
        return hash((self.title, self.author))

# Now Python can use your custom object in a set safely!
library = {Book("1984", "George Orwell")}


# Set methods
my_set = {1, 2, 3}

# .add(x) -> Adds an element to the set. If it already exists, nothing happens.
my_set.add(4)  # {1, 2, 3, 4}

# .remove(x) -> Removes x. CRASHES with a KeyError if x is not in the set.
my_set.remove(2)  # {1, 3, 4}

# .discard(x) -> Removes x. Safe to use because it does NOT crash if x is missing.
my_set.discard(99)  # Quietly does nothing

# WARNING: set.pop() removes an ARBITRARY element, not the "first" one.
# It looks ordered with small positive integers because of how they are bucketed in memory,
# but with strings or mixed data, it is completely unpredictable!
popped_val = my_set.pop()  

# .clear() -> Empties the entire set.
my_set.clear()  # set()


