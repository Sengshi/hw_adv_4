class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.new_list = self.list_of_list.__iter__()
        self.position = 0
        self.list_position = 0
        self.cursor = 0
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
                    # if isinstance(item, list):
                    while isinstance(item, list):
                        if self.cursor < len(item):
                            new_item = item[self.cursor]
                            while isinstance(new_item, list):
                                new_item = new_item[0]
                            self.cursor += 1
                            return new_item
                        else:
                            self.position += 1
                            self.cursor = 0
                            break
                    else:
                        self.position += 1
                        return item
            else:
                raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    # вывод для теста
    print(list(FlatIterator(list_of_lists_2)))


if __name__ == '__main__':
    test_3()
