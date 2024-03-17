import math
import sys
import random

print(math.e)

wynik1 = math.sqrt(27 * (1.0/3))
print(wynik1)

wynik0 = math.sqrt((math.e**2 - math.log2(34)) * (1.0/3))
print(wynik0)

wynik2 = math.sqrt((math.log(20) + math.cos(45) + math.e) * 1.0/3)
print(wynik2)

wynik3 = math.sqrt((math.log(20, 3) + math.sin(45) * (5/8)) * 1.0/4)
print(round(wynik3, 2))

def wieza():
    a = int(input("Podaj wysokosc wiezy (max 10): "))
    if(a<=10):
        for i in range (1, a+1):
            print("A"*i)
    else:
        print("Wartosc wieksza od 10!")



wieza()

def licz_slowa():

    napis = str(input("Podaj napis: "))
    slowa = napis.split()
    print (len(slowa))

licz_slowa()

def potega():
    sys.stdout.write("Podaj pierwsza liczbe calkowita: ")
    sys.stdout.flush()
    a = int(sys.stdin.readline())

    sys.stdout.write("Podaj pierwsza liczbe calkowita: ")
    sys.stdout.flush()
    b = int(sys.stdin.readline())

    sys.stdout.write("Podaj pierwsza liczbe calkowita: ")
    sys.stdout.flush()
    c = int(sys.stdin.readline())

    dzialanie = (a**b) + c

    sys.stdout.write("Wynikiem obliczenia {} ** {} + {} = {}\n".format(a,b,c, dzialanie))
    sys.stdout.flush()

potega()

def palindrom():
    napis = str(input("Podaj napis brachu: "))
    if napis == napis [::-1]:
        print("To palindorm")
    else:
        print("Nie jest mordo")

palindrom()

def czy_pierwsza():
    liczba = int(input("Podaj liczbę, a my sprawdzimy czy jest pierwsza: "))
    if (liczba>2 and liczba%2 == 0):
        print("Liczba nie jest pierwsza")
    else:
        print("Liczba jest pierwsza! Udało nam sie")

czy_pierwsza()

def czy_doskonala():
    suma = 0
    lista = []
    for i in range(1,1001):
        for x in range(1, i):
            if i%x==0:
                suma = suma + x
                if suma == i and x >= suma/2:
                    lista.append(i)
                    suma = 0
                elif (x==i-1 and suma !=i):
                    suma = 0
            elif (x==i-1 and suma !=i):
                suma = 0
    print(lista)

czy_doskonala()

def wektor():
    n = int(input("Podaj ilosc wierszy: "))
    suma_a = 0
    suma_b = 0
    for i in range(1, n+1):
        a = random.randint(1, 101)
        b = random.randint(1, 101)
        suma_a = suma_a + a
        suma_b = suma_b + b
        print(a,"x",b)
    print("Suma wszystkich wierszy wynosi: ",suma_a,"x", suma_b)

wektor()


def wektor1():
    suma_sum = 0
    n = int(input("Podaj ilosc wierszy i kolumn: "))
    for i in range(1, n+1):
        wektor = []
        for x in range(n):
            wektor.append(random.randint(1, 101))
        print(wektor)
        suma = 0
        for l in wektor:
            suma = suma + l
        print(suma)
        suma_sum = suma_sum + suma
    print (suma_sum)







wektor1()
