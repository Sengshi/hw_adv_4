class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_position = 0
        self.position = 0

        return self

    def __next__(self):
        while True:
            if self.list_position < len(self.list_of_list):
                if self.position >= len(self.list_of_list[self.list_position]):
                    self.list_position += 1
                    self.position = 0
                    continue
                else:
                    item = self.list_of_list[self.list_position][self.position]
                    self.position += 1
                    return item
            else:
                raise StopIteration


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
    # проверка
    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()
