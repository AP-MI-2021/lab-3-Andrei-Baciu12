def main():
    stop = False
    while not stop:
        print("""
            1 -> Citeste lista
            2 -> Afiseaza cea mai lunga secventa de numere pare
            3 -> Afiseaza cea mai lunga secventa de numere prime obtinute prin concatenarea elementelor listei
            4 -> Afiseaza cea mai lunga secventa de numere cu acelasi numar de biti de 1
            x -> Exit
        """)
        optiune = input("Alege optiune: ")
        if optiune == '1':
            list = citeste_lista()
            print(list)
        elif optiune == 'x':
            stop = True
        elif optiune == '2':
            list = citeste_lista()
            list2 = get_longest_all_even(list)
            print(f'cea mai lunga secventa de numere pare este {list2}')
        elif optiune == '3':
            list = citeste_lista()
            list3 = get_longest_concat_is_prime(list)
            print(list3)
        elif optiune == '4':
            list = citeste_lista()
            list4 = get_longest_same_bit_counts(list)
            print(list4)
        else:
            print("Optiune invalida!")


def citeste_lista():
    result = []
    string_lista = input("Introduceti lista: ")
    string_elemente = string_lista.split(sep=" ")
    for string_element in string_elemente:
        element = int(string_element)
        result.append(element)
    return result


def are_elemente_pare(list):
    for element in list:
        if element % 2 != 0:
            return False

    return True


def get_longest_all_even(list):
    """
    Functia gaseste cea mai lunga subsecventa de numere pare dintr-o lista introdusa


    :param list:o lista de numere intregi
    :return: lista de numere pare
    """
    result_list = []
    for start in range(0, len(list)):
        for end in range(start + 1, len(list) + 1):
            if are_elemente_pare(list[start:end + 1]):
                result_list.append(list[start:end + 1])
    max_sec = []
    for secventa in result_list:
        if len(secventa) > len(max_sec):
            max_sec = secventa
    return max_sec

def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 3, 4, 6]) == [4, 6]
    assert get_longest_all_even([1, 2, 3, 4, 6, 8, 10, 12]) == [4, 6, 8, 10, 12]

test_get_longest_all_even()

def get_longest_concat_is_prime(list):
    """
    Functia gaseste cea mai lunga secventa in care concatenarea elementelor ei este un numar prim


    :param list:lista de intregi
    :return:o lista de numere a caror concatenare este un numar prim
    """
    secv_max = []
    for start in range(0, len(list)):
        for end in range(start, len(list)):
            if concatenare_elemente_is_prime(list[start:end + 1])  and len(list[start:end + 1]) > len(secv_max):
                secv_max = list[start:end + 1]
    return secv_max

def concatenare_elemente(list):
    """
    Functia concateneaza toate elementele listei si returneaza numarul obtinut

    :param list: o lista de intregi
    :return: numarul obtinut prin concatenarea elementelor listei
    """
    s = [str(i) for i in list]
    res = int("".join(s))
    return res


def concatenare_elemente_is_prime(list):
    n = concatenare_elemente(list)
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([1, 2, 3, 4, 5, 6]) == [2, 3]
    assert get_longest_concat_is_prime([1, 2, 3, 11, 13, 17, 113]) == [2, 3, 11]

test_get_longest_concat_is_prime()


def get_longest_same_bit_counts(list):
    """
    Functia determina cea mai lunga secventa a unei liste care are elementele cu acelasi numar de biti de 1

    :param list: o lista de numere intregi si pozitive
    :return: o lista de numere cu acelasi numar de biti de unu
    """
    max_sec2 = []
    for start in range(0, len(list) + 1):
        for end in range(start + 1, len(list) + 1):
            if are_acelasi_nr_biti(list[start:end + 1]) and len(list[start:end + 1]) > len(max_sec2):
                max_sec2 = list[start:end + 1]
    return max_sec2



def numar_de_biti_de_unu(n):
    c = 0
    while n > 0:
        if n % 2 == 1:
            c += 1
        n = n // 2
    return c


def are_acelasi_nr_biti(list):
    contor = numar_de_biti_de_unu(list[0])
    for element in list:
        if numar_de_biti_de_unu(element) != contor:
            return False
    return True

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([1, 2, 3, 4, 5]) == [1, 2]
    assert get_longest_same_bit_counts([2, 4, 8, 16, 32, 50]) == [2, 4, 8, 16, 32]

test_get_longest_same_bit_counts()


main()
