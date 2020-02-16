# text = 'I love Python!'
#
# print(len(text))
# print(text.__len__())


class SomeList:
    def __init__(self):
        self._inner_list = []

    def add_element(self, element):
        self._inner_list.append(element)

    def remove_element(self, element):
        self._inner_list.remove(element)

    def __len__(self):
        return len(self._inner_list)


some_list = SomeList()
some_list.add_element(1)
some_list.add_element(2)
some_list.add_element(3)
print(len(some_list))
print(some_list.__len__())