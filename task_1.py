# W tym zadaniu wcielisz się w skrybe (a do tego lenia i plagiatora) ciągów znakowych.
# Skryba dostał zadanie stworzenia nowego ciągu znakowego. Nie chce mu się poświęcać
# na to zbyt dużo czasu więc postanowił wykorzystać ciągi znakowe ze swojej biblioteczki.
#
# Skryba działa metodycznie i chce całkowicie wykorzystać potencjał swojej kolekcji ciągów.
# Wypracował następujący schemat działania:
# 1. Bierze pierwszy ciąg z bilioteczki
# 2. Przepisuje pierwszy znak z pobranego z bilbioteczki ciągu do ciągu, który właśnie tworzy
# 3. Zapamiętuje, że wykorzystał już pierwszy znak z pierwszego ciągu
# 4. Przechodzi do kolejnego ciągu, wybiera go zgodnie z kolejnościa przechowywania ciągów w
#    biblioteczce
# 5. Kopiuje z pobranego ciągu pierwszy znak, którego jeszcze nie wykorzystał z danego ciągu i
#    i zapamiętuje który znak wykorzystał
# 6. Powtarza kroki 4 i 5, jeśli dojdzie do końca bilbioteczki to wraca na jej początek i powtarza
#    proces tak długo, aż wykorzysta wszystkie znaki ze wszystkich dostępnych w bilbioteczce ciągów
#
# Dodatkowo z racji tego, że jest leniwy, kompresuje w tworzonym ciągu powtarzające się znaki
# zastępując je liczbą kolejnych wystąpień tego samego znaku połączoną z samym znakiem
# np. "aaaaaaa" -> "7a"
#
# Przykład:
# Skryba ma w swojej bilbioteczce (`sources`) następujące ciągi znakowe:
# `sources = ["python", "java", "golang"]`
#
# Jego genialna i nowatorska metoda tworzenia nowych ciogów zaowocuje następującym ciągiem:
# `result = "pjgyaotvlh2ao2ng"`
#
# Pomóż skrybie zautomatyzowac ten proces! Rezultat przypisz do zmiennej `result`.
# * W liście `sources` znajdują się ciągi znakowe które odpowiadają bilbioteczce skryby.
# * Ciągi znakowe w 'sources' składają się wyłącznie ze znaków a-z.
# * Znaki traktuj jako unikalne podmioty, wykorzystanie znaku 'a' z któregoś z ciągów z
#   z biblioteczki nie oznacza, że nie można wykorzystać znaku 'a' znajdującego się
#   dalej w tym samym ciągu


def lazy_scribe(sources: list):
    result: str = ''
    number_of_characters_in_longest_string = len(max(sources, key=len, default=''))
    index = 0
    flag = True

    while flag:
        if not number_of_characters_in_longest_string:
            return result
        else:
            for word in sources:
                if len(word) > index:
                    result += word[index]
                if number_of_characters_in_longest_string == index:
                    compressed_result = ''
                    index = 0

                    while index != len(result):
                        number_of_occurrences = 1
                        while (index < len(result) - 1) and (result[index] == result[index + 1]):
                            number_of_occurrences += 1
                            index += 1
                        if number_of_occurrences == 1:
                            compressed_result += str(result[index])
                        else:
                            compressed_result += str(number_of_occurrences) + str(result[index])
                        index += 1
                    result = compressed_result
                    flag = False
        index += 1
    return result


def test_lazy_scribe():
    assert lazy_scribe(["python", "java", "golang"]) == "pjgyaotvlh2ao2ng"
    assert lazy_scribe([]) == ""
    assert lazy_scribe([""]) == ""
    assert lazy_scribe(["", "", "", ""]) == ""
    assert lazy_scribe(["a", "b", "c", "d"]) == "abcd"
    assert lazy_scribe(["yomasoul", "yomaha", "yoma", "tyryryryry", "ryry"]) == "3ytr3o2y3m2r3a2yshroayurlyry"
