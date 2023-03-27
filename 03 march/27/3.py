import itertools


class PaginationHelper:

    def __init__(self, collection: list, items_per_page: int) -> None:
        self.collection = collection
        self.items_per_page = items_per_page
        it = iter(collection)
        self.item_pages = list(
            iter(lambda: tuple(itertools.islice(it, items_per_page)), ())
        )

    def item_count(self) -> int:
        return len(self.collection)

    def page_count(self) -> int:
        return len(self.item_pages)

    def page_item_count(self, page_index: int) -> int:
        try:
            return len(self.item_pages[page_index])
        except IndexError:
            return -1

    def page_index(self, item_index: int) -> int:
        for part in self.item_pages:
            try:
                if self.collection[item_index] in part:
                    return self.item_pages.index(part)
            except IndexError:
                return -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # повинно == 2
print(helper.item_count())  # повинно == 6
print(helper.item_pages)
print(helper.page_item_count(0))  # повинно == 4
print(helper.page_item_count(1))  # остання сторінка - повинна == 2
print(helper.page_item_count(2))  # повинно == -1, тому що сторінка недійсна
#
# # page_index приймає індекс елемента та повертає сторінку, якій він належить
print(helper.page_index(5))  # повинен == 1 (індекс з відліком від нуля)
print(helper.page_index(2))  # повинен == 0
print(helper.page_index(20))  # повинно == -1
print(helper.page_index(-10))  # повинно == -1, тому що негативні індекси недійсні
