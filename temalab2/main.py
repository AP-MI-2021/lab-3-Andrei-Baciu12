def main():
    stop = False
    while not stop:
        print("""
            1 -> Verificarea conjecturii lui Goldbach
            2 -> Determinarea valorii unui radical prin metoda lui Newton
            3 -> Verificarea faptului ca un numar este palindrom
            x -> Exit
        """)
        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            numar = int(input("Introduceti un numar par mai mare decat 2: "))
            pr1, pr2 = get_goldbach(numar)
            print(f'{numar} este egal cu suma dintre {pr1} si {pr2}')
        elif optiune == '2':
            numar = int(input("Introduceti un numar pozitiv: "))
            stepss = int(input("Introduceti un numar de pasi:"))
            valoareradical = get_newton_sqrt(numar, stepss)
            print(f'Valoarea radicalului lui {numar}, obtiunuta prin {stepss} pasi este {valoareradical}')
        elif optiune == '3':
            numar = int(input("Introduceti un numar intreg: "))
            if is_palindrome(numar):
                print(f'numarul {numar} este palindrom')
            else:
                print(f'numarul {numar} nu este palindrom')
        elif optiune == 'x':
            stop = True
        else:
            print("optiune invalida!")
            break

def get_goldbach(n) -> (int, int):
    """
    Functia determina doua numere prime, prim1 si prim2 astfel incat prim1 + prim2 = n, unde n este numar par mai mare decat 2.

    :param n: un numar par mai mare ca 2
    :return:prim1, prim2
    prim1 - min
    prim2 - max
    """

    prim1 = 3
    prim2 = n - prim1
    while prim1 <= prim2:
        if is_prime(prim1) and is_prime(prim2):
            return prim1, prim2
        prim1 = prim1 + 2
        prim2 = n - prim1


def is_prime(nr):
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True
def test_get_goldbach():
    assert get_goldbach(10) == (3, 7)
    assert get_goldbach(20) == (3, 17)

def get_newton_sqrt(n, steps) -> float:
    """
    Functia gaseste valoarea radicalului unui numar pozitiv prin metoda lui Newton, printr un anumit numar de pasi.


    :param n: un numar pozitiv
    :param steps: un numar intreg pozitiv
    :return: valoarea radicalului
    """
    x0 = 2
    while steps > 0:
        valoarea_radicalului = x0 - ((x0 ** 2) - n) / (2 * n)
        x0 = valoarea_radicalului
        steps = steps - 1
    return valoarea_radicalului



def test_get_newton_sqrt():
    assert get_newton_sqrt(4, 100) == 2
    assert get_newton_sqrt(15, 3) == 2.9405562468678554



def is_palindrome(n) -> bool:
    temp = n
    rest = 0
    while n > 0:
        cifra = n % 10
        rest = rest * 10 + cifra
        n = n // 10
    if temp != rest:
        return False
    return True


def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(12) is False


test_get_goldbach()
test_get_newton_sqrt()
test_is_palindrome()

main()