# Zadeklaruj klasę `Bee`
# * Klasa przyjmuje dwa argumenty `name` i `identifier` podczas
#   instancjonowania
# * Klasa jest konwertowalna do typu `string`, to znaczy wywołanie
#   `str(bee)` zwraca wartość typu `string` o określonym formacie
#   i zawartości
# * Format wyżej wymienionej wartości wygląda następująco: `{identifier} {name}`,
#   dla `bee = Bee(name='Bumble', identifier=1)` wywołanie `str(bee)` zwróci `"1 Bumble"`
# * Obiekty klasy `Bee` mają metodę `get_hive()` zwracającą zbiór tekstowych
#   reprezentacji wszyskich utworzonych instancji klasy Bee

class Bee:
    _instances = []

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.get_hive()

    def get_hive(self):
        self._instances.append(str(self))
        return set(self._instances)

    def __str__(self):
        return f'{self.identifier} {self.name}'


def test_get_hive():
    bee1 = Bee(name="Maja", identifier=222)
    bee2 = Bee(name="Gucio", identifier=4234)

    assert str(bee1) == "222 Maja"
    assert str(bee2) == "4234 Gucio"
