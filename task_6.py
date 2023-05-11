# Poniżej znajdują się deklaracje klas `StockItem` i `StockSorter`.
# Klasa `StockSorter` służy do sortowania obiektów klasy `StockItem`
# jako klucz sortowania wykorzustując atrybut `sku`.
#
# Zadeklaruj klasę `StockQuantitySorter`, dziedziczącą po `StockSorter`
# i definiującą jedną metodę. Klasa ta ma działać analogicznie do `StockSorter`
# jako klucz sortowania wykorzystując atrybut `quantity`
#
# * Nie nadpisuj metody `sort`

from typing import List


class StockItem:
    def __init__(self, sku: str, quantity: int):
        self.sku = sku
        self.quantity = quantity


class StockSorter:
    def sort(self, stock: List[StockItem]):
        sorted_stock = sorted(stock, key=self._get_sorting_key)
        return sorted_stock

    def _get_sorting_key(self, stock_item: StockItem):
        return stock_item.sku


# Tutaj zadeklaruj klasę `StockQuantitySorter`
class StockQuantitySorter(StockSorter):

    def _get_sorting_key(self, stock_item: StockItem):
        return stock_item.quantity


class TestStockSorters():
    def test_default_case(self):
        assert isinstance(StockQuantitySorter, type)
        assert issubclass(StockQuantitySorter, StockSorter)

    def test_stock_sorter(self):
        item_a = StockItem("a", 100)
        item_b = StockItem("b", 50)
        item_c = StockItem("c", 110)

        stock = [item_c, item_a, item_b]
        sorted_stock = [item_a, item_b, item_c]

        stock_sorter = StockSorter()

        assert sorted_stock == stock_sorter.sort(stock)

        quantity_sorted_stock = [item_b, item_a, item_c]
        stock_quantity_sorter = StockQuantitySorter()

        assert quantity_sorted_stock == stock_quantity_sorter.sort(stock)
