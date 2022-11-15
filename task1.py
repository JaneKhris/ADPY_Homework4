class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.count1 = 0
        self.count2 = 0
        return self

    def __next__(self):
        if self.count1 >= len(self.list):
            raise StopIteration
        else:
            if type(self.list[self.count1]) == list:
                if self.count2 >= len(self.list[self.count1]) and self.count1 == (len(self.list)-1):
                    raise StopIteration
                elif self.count2 >= len(self.list[self.count1]):
                    self.count2 = 0
                    self.count1 += 1
                item = self.list[self.count1][self.count2]
                self.count2 += 1
            else:
                item = self.list[self.count1]
                self.count1 += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
