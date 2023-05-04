# Napisz kalkulator tak, aby był w stanie
# wykonać działanie dowolnej długości.
#
# Przykład:
# calculator(1)('+')(4)('-')(2)('=') == 3
#
# * Kalkulator musi wspierać działania dodawania
#   i odejmowania
# * Każde działanie kończy się znakiem '='
# * Nie korzystaj ze zmiennych globalnych i importów


def calculator(x):
    def symbol(s):
        if s == '=':
            return x

        def operation(y):
            if s == '+':
                result = x + y
                return calculator(result)
            elif s == '-':
                result = x - y
                return calculator(result)
            return operation

        return operation

    return symbol

