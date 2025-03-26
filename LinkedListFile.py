import logging
import datetime
from operator import truediv
from typing import Generic, TypeVar, List, Optional
T = TypeVar("T")


# logging.basicConfig(level=logging.INFO) # simple version to the output console
logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file called log.txt in your project


class LL_Node(Generic[T]):
    def __init__(self, value: T = None, next_node: Optional["LL_Node[T]"] = None):
        self.next_node = next_node
        self.value = value

    def has_next(self):
        return self.next_node is not None

    def get_next(self) -> Optional["LL_Node[T]"]:
        return self.next_node

    def get_value(self) -> T:
        return self.value

    def set_value(self, in_val: T):
        self.value = in_val

    def set_next(self, nxt: Optional["LL_Node[T]"]):
        self.next_node = nxt


class LinkedList(Generic[T]):
    def __init__(self):
        self.start: Optional[LL_Node[T]] = None

    def is_empty(self):
        return self.start is None

    @log_start_stop_method
    def add_to_end(self, item: T):
        """
        appends a node with the given value at the end of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        # OK, I've written this one for you, to get you started.
        if self.start is None:
            self.start = LL_Node[T](value=item)
        else:
            p: LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            p.set_next(LL_Node[T](value=item))

    def add_to_start(self, item: T):
        """
        inserts a node with the given value at the start of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            self.start = LL_Node[T](value=item)
        else:
            p: LL_Node[T] = self.start
            self.start = LL_Node[T](value=item, next_node = p)
        # ------------------------------

    def add_all_to_end(self, items: List[T]):
        """
        appends each of the items in items as separate nodes at the end of this list, preserving order.
        Note: while you can call other methods, it might not be the most efficient!
        :param items: a list or tuple of items to add
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            for i in items:
                self.add_to_end(i)
        else:
            p: LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            for i in items:
                p.set_next(LL_Node[T](value=i))
                p = p.get_next()
        # ------------------------------

    def __len__(self):
        """
        overrides the "len" operator - gives the number of items in this list.
        :return: the number of items
        """
        length = 0
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            pass
        else:
            length = length + 1
            p: LL_Node[T] = self.start
            while p.has_next():
                length = length + 1
                p = p.get_next()
        # ------------------------------
        return length

    def __contains__(self, item):
        """
        returns whether this linked list contains the item, at least once.
        :param item: the item to match
        :return: whether this item is in the linked list.
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            pass
        else:
            p: LL_Node[T] = self.start
            i = 0
            while self.__len__()>i:
                if p.get_value() == item:
                    return True
                p = p.get_next()
                i += 1
        # ------------------------------
        return False

    def index(self, item):
        """
        gives the index of the first instance in this list with matching item, or throws an error if not found.
        :param item: item to match
        :return: the positive index of the first occurrence of the item.
        """
        # ------------------------------
        # DONE: You write this one
        if self.__contains__(item):
            p: LL_Node[T] = self.start
            length = 0
            i = 0
            while self.__len__() > i:
                if p.get_value() == item:
                    return length
                length += 1
                p = p.get_next()
                i += 1
        # ------------------------------
        else:
            raise RuntimeError(f"Item {item} not found in list.")

    def pointers_for_index(self, index: int) -> {Optional[LL_Node[T]], Optional[LL_Node[T]]}:
        """
        Internal method - not really intended for an outside class to use this, but other methods in this class may
        find it handy!

        Gets the pointer to the ith item in the list and the pointer to the (i-1)th item in the list. If "i" is zero,
        then the latter will be None. If "i" extends 1 past the end of the list, p will be None and back will be the
        last element. If "i" extends further than that past the end of the list, then both will be None.
        :param index: a non-negative integer
        :return: p, back - the pointers for the ith and (i-1)th items in the list.
        """
        # OK. I've written this one for you.
        p: Optional[LL_Node[T]] = self.start
        back: Optional[LL_Node[T]] = None
        count = 0
        while count < index:
            back = p
            if p is not None:
                p = p.get_next()
            count += 1
            if p is None and back is None:
                break
        return p, back

    def item_at_index(self, index: int) -> T:
        """
        gets the item stored in the list at position "index." Does not alter the list. Crashes if index is out of range.
        :param index: an index in range 0 ... len(list)-1, inclusive
        :return: the value stored in the list at this location.
        """
        # ------------------------------
        # DONE: You write this one - I suggest you make use of self.pointers_for_index, which I wrote for you just
        #  before this one.
        p, back = self.pointers_for_index(index)
        if p is not None:
            return p.get_value()
       # elif back is not None:
       #     return back.get_value()
        else:
            raise IndexError(f"Index out of range: {index}.")
        # ------------------------------
        # return p.value  # replace this to return an actual value.

    def item_at_start(self) -> T:
        """
        gets the value stored in the first node
        :return: value
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            pass
        else:
            return self.start.get_value()
        # ------------------------------

    def item_at_end(self) -> T:
        """
        gets the value stored in the last node.
        (Tip: remember, counting up the nodes is O(N)... try to avoid making two passes through this list.)
        :return:
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            return self.start.get_value()
        else:
            p: LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            return p.get_value()
        # ------------------------------
        # return p.value  # replace this to return an actual value.

    def insert_value_at_start(self, value: T):
        """
        creates a new node with value and inserts it at the start of the list.
        :param value: item to add.
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        p, back = self.pointers_for_index(0)
        if p == self.start:
            self.add_to_start(value)
        else:
            back.next_node = LL_Node[T](value=value, next_node=p)
        # ------------------------------

    def insert_value_at_index(self, value: T, index: int):
        """
        puts the given value into a new node and inserts it into the list so that it is now at position "index." If
        index > length of the list, this will put it at the end of the list.
        :param value:
        :param index:
        :return:
        """
        # I've written this one for you.
        p, back = self.pointers_for_index(index)
        if p == self.start:
            self.insert_value_at_start(value)
        else:
            back.next_node = LL_Node[T](value=value, next_node=p)

    def insert_all_at_index(self, in_list: List[T], index: int):
        """
        Goes through all the items in list, and adds them (in order) into this list, starting at the initial location.
        :param in_list:
        :param index:
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        i = 0
        while i<len(in_list):
            p, back = self.pointers_for_index(index+i)
            if back is not None:
                self.insert_value_at_index(in_list[i], index+i)
            elif index == 0:
                self.insert_value_at_start(in_list[i])
            else:
                raise IndexError("Index out of range.")
            i += 1


        #    self.insert_value_at_index(in_list[index], index)
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_first_item(self):
        """
        alters this list by removing the first item. If there is no first item, then throws an exception
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            raise IndexError("Index out of range.")
        else:
            p: LL_Node[T] = self.start
            self.start = p.get_next()
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_item_at_index(self, index: int):
        """
        alters this list by removing the ith element. If index is out of the range of the list, throws an exception.
        :param index: item number to remove
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        p, back = self.pointers_for_index(index)
        if self.start is None or self.__len__()-1<index:
            raise IndexError("Index out of range.")
        elif index == 0:
            self.remove_first_item()
        elif p is not None:
            back.set_next(p.get_next())
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_last_item(self):
        """
        removes the last item in this list, but does not return it. If list is empty, throw an exception
        (Note, since counting up the number of items in the list is O(N), try to avoid making two passes.)
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        p, back = self.pointers_for_index(self.__len__()-1)
        if self.start is None:
            raise IndexError("Index out of range.")
        else:
            p: LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            back.set_next(p.get_next())
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove(self, val: T, first_only=False):
        """
        removes either the first or all items that match val from this list, depending on the state of first_only
        :param val:
        :param first_only:
        :return: None
        """
        # ------------------------------
        # DONE: You write this one
        if self.start is None:
            pass
        else:
            if self.__contains__(val):
                if first_only:
                 self.remove_item_at_index(self.index(val))
                else:
                    while self.__contains__(val):
                        self.remove_item_at_index(self.index(val))

        # ------------------------------

    def to_list(self) -> List[T]:
        """
        generates a list of items in the same order as this linked list.
        """
        # I've written this one for you.
        result = []
        p: Optional[LL_Node[T]] = self.start
        while p is not None:
            result.append(p.get_value())
            p = p.get_next()
        return result

    def __str__(self) -> str:
        """
        This is akin to the "toString()" method in java - this makes a string representation of this list.
        :return: a string describing this list.
        """
        result = "["
        p: Optional[LL_Node[T]] = self.start
        while p is not None:
            result += f"{p.get_value()} "
            p = p.get_next()
        result += "]"
        return result

    def __repr__(self) -> str:
        """
                This is akin to the "toString()" method in java - this makes a string representation of this list.
                (For debugging.)
                :return: a string describing this list.
                """
        return self.__str__()  # in this case, the __repr__ and __str__ are the same.