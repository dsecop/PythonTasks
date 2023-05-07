# Zadeklaruj klasę `Colony` i `Ant`
# * Klasa `Colony` przyjmuje argument `name` podczas
#   instancjonowania
# * Obiekty klasy `Colony` posiadają atrybut `name`
#   co do wartości odpowiadający argumentowi przekazanemu podczas
#   instancjonowania
# * Obiekty klasy `Colony` posiadają metodę `spawn_ant` przyjmującą
#   argument `name` i zwracającą obiekt klasy `Ant`. Wartość atrybutu
#   `name` utworzonego obiektu odpowiada wartości przekazanego argumentu
# * Obiekty klasy 'Colony' posiadają atrybut 'ants' będący zbiorem
#   wszystkich obiektów typu `Ant` utworzonych przez wywołania metody
#   `spawn_ant`
# * Obiektu klasy `Ant` posiadają atrybuty `name` i `colony` odpowiadające
#   kolejno argumentowi `name` przekazanemu do `spawn_ant` oraz obiektowi
#   colony na którym ta metoda została wywołana
# * Kod testujący tworzy obiektu `Ant` tylko poprzez wywołania metody `spawn_ant`
#
#  Przykład:
#  colony = Colony("MyColony")
#  worker = colony.spawn_ant("worker")
#  worker.name == "worker"
#  worker.colony == colony
#  colony.ants == {worker}
#  worker2 = colony.spawn_ant("worker2")
#  colony.ants == {worker, worker2}

class Colony:
    def __init__(self, name):
        self.name = name
        self.ants = set()

    def spawn_ant(self, name):
        obj = Ant(name, self)
        self.ants.add(obj)
        return obj

    def __str__(self):
        return f'{self.name}'


class Ant:
    def __init__(self, name, colony=None):
        if colony is None:
            self.colony = {}
        self.colony = colony
        self.name = name

    def __str__(self):
        return f'{self.name}'


class TestAntColony:
    def test_default_case(self):
        assert isinstance(Colony, type)
        assert isinstance(Ant, type)

    def test_empty_colony(self):
        colony = Colony("my-colony")
        assert colony.ants == set()
        assert colony.name == "my-colony"

    def test_ant_spawning(self):
        colony = Colony("my-colony")
        worker = colony.spawn_ant("worker")
        assert worker.name == "worker"
        assert worker.colony == colony
        assert colony.ants == {worker}

    def test_multiple_colonies(self):
        colony_alpha = Colony("alpha")
        colony_beta = Colony("beta")
        alpha_worker = colony_alpha.spawn_ant("worker")

        assert alpha_worker.colony == colony_alpha
        assert colony_alpha.ants == {alpha_worker}
        assert colony_beta.ants == set()

        beta_worker = colony_beta.spawn_ant("worker")
        assert beta_worker.colony == colony_beta
        assert colony_alpha.ants == {alpha_worker}
        assert colony_beta.ants == {beta_worker}

    def test_multiple_ants(self):
        colony = Colony("my-colony")
        assert colony.ants == set()

        workers = [
            colony.spawn_ant("worker_alpha"),
            colony.spawn_ant("worker_beta"),
            colony.spawn_ant("worker_gamma"),
        ]

        for worker in workers:
            assert worker.colony == colony

        assert colony.ants == set(workers)
