# Uzupełnij funkcję `simple_functional_calc` aby za pomocą
# kolejnych wowołań dało się wykonywać operację dodawania i
# odejmowania. Pierwsze wywołanie będzie zawierało wartość
# pierwszego operandu, drugie wywołanie będzie zawierało
# znak reprezentujący operację a trzecie wywołanie będzie
# zawierało wartość drugiego operandu. Operacją może być
# dodawanie ('+') lub odejmowanie ('-').
#
# Przykład 1:
# simple_functional_calc(1)('+')(1) == 2
#
# Przykład 2:
# simple_functional_calc(1)('-')(1) == 0
#


def simple_functional_calc(x):
    def symbol(s):
        def operation(y):
            if s == '+':
                result = x + y
            else:
                result = x - y
            return result
        return operation
    return symbol

