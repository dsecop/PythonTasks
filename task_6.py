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
