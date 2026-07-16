class ListItem:
    """A List item, which is a simple container for a single value.
    """
    def __init__(self, value):
        self.value = value


class CustomList:
    """A custom list implementation using tuples.
    """
    def __init__(self):
        # A counter of how many items the list has
        self.list_length = 0

        # Pre-allocate a tuple of size 1 filled with None
        self.tuple_size = 1
        self.items = (ListItem(None),)

    def append(self, value):
        # Set the first empty spot in the pre-allocated array
        self.items[self.list_length].value = value
        self.list_length += 1

        self._check_grow() # Check if the list can grow and grow it

    def pop(self):
        # pop from the end and store the popped item
        result = self.items[self.list_length - 1].value

        # Set the popped value to `None` and decrease the list_length
        self.items[self.list_length - 1].value = None
        self.list_length -= 1

        self._check_shrink() # Check if the list can shrink and shrink it
        return result

    def _check_grow(self):
        # If the internal tuple is filled, increase its size by a factor of 2
        if self.list_length == self.tuple_size:
            self._resize(self.tuple_size * 2)

    def _check_shrink(self):
        # If there's too much empty space, decrease the size by a factor of 2
        if self.list_length <= self.tuple_size / 2:
            self._resize(int(self.tuple_size / 2))

    def _resize(self, new_size):
        if new_size <= 0:
            return

        old_items = self.items # save a reference to the old items

        # Create a new tuple of given size
        self.items = tuple(ListItem(None) for _ in range(new_size))
        self.tuple_size = new_size

        # Copy all items to the new tuple.
        for idx in range(self.tuple_size):
            if idx >= len(old_items): # Break if no more old_items left
                break
            self.items[idx].value = old_items[idx].value

    def __repr__(self):
        return '[' + ','.join([
            str(item.value) for item in self.items
            if item.value is not None
        ]) + ']'

    def insert(self, index, value):
        # Shift all items right of the index
        for idx in reversed(range(index, self.list_length)):
            self.items[idx + 1].value = self.items[idx].value

        self.items[index].value = value
        self.list_length += 1

        self._check_grow() # Check if the list can grow and grow it
