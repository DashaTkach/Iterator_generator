class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.index = 0
        self.new_list = []
        return self

    def __next__(self):
        if self.index >= len(self.list_of_list):
            raise StopIteration
        for i in self.list_of_list[self.index]:
            self.new_list.append(i)
        self.index += 1
        return self.new_list


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(list_of_lists_1):
        item = item

    for flat_iterator_item, check_item in zip(
            item,
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(item) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
