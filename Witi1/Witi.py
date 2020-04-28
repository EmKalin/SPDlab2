import os
import math
import time
import heapq
import copy
import itertools


def pobierz_dane(plik):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plik):  # sprawdzamy czy plik istnieje na dysku
        with open(plik, "r") as zawartosc:  # otwieramy plik do odczytu
            i = 0
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                x = map(int, linia.split(" "))   # dodajemy elementy do tupli a tuplę do listy
                x = list(x)                      # tutaj takie wygibasy żeby dodać czwarta liczbę
                x.append(i)                      # która jest kolejnością zadań
                dane.append(list(x))            # pewnie da się ładniej ale jestem nowy w Python
                i = i + 1                        # i++ zadania są numerowane od 1 do n
    else:
        print("Plik z danymi", plik, "nie istnieje!")
    return list(dane)  # przekształcamy listę na tuplę i zwracamy ją


def kolejnosc(lista):
    y = []
    for item in lista:
        y.append(item[3])
    return y



def calculate(tablica,n):
    S=0
    C=tablica[0][0]
    T=max(C-tablica[0][2],0)
    F=tablica[0][1]*T

    for i in range (1,n):
        S = C
        C = S + tablica[i][0]
        T = max(C - tablica[i][2],0)
        K = T*tablica[i][1]
        F = F + K

    return F

def bruteforce(tablica, wynik, krok = 0):
    if krok == len(tablica):
        wynik.append(tablica)                                                       # koniec, dodaj permutacje
    for i in range(krok, len(tablica)):
        tablica_copy = [c for c in tablica]                                         # skopiuj tablice
        tablica_copy[krok], tablica_copy[i] = tablica_copy[i], tablica_copy[krok]   # zamien aktualny indeks z krokiem
        bruteforce(tablica_copy, wynik, krok + 1)                                   # rekurencja

def BF(tablica):
    wynik = []
    bruteforce(tablica, wynik)
    return wynik

def permut(tablica, n):
    #wynik = list(itertools.permutations(tablica))
    wynik = BF(tablica)
    P = 100000
    for i in range(0, math.factorial(n)):
        kolej = wynik[i]
        K = calculate(kolej, n)
        P = min(P, K)

    return P

def dynamicW(tablica):
    C = 0
   # x=bin(2**10-1)

    # print(x[2:])

   # n = len(tablica)

    for i in range(0, len(tablica)):
        C = C+tablica[i][0]


    fin=[]

    for j in range(0, len(tablica)):

        G = copy.deepcopy(tablica)
        K = G[j][1]*max(C-G[j][2], 0)

        if len(G)>1:
            G.pop(j)
            fin.append(dynamicW(G)+K)
        else:
            fin.append(K)

    opt = min(fin)

    return opt


def zad1(pliki):
    for j in range(0, len(pliki)):
        dane = pobierz_dane(pliki[j])
        n = dane[0][0]
        r = dane[0][1]
        dane = list(dane[1:n + 1])
        start = time.time()
        wynik = calculate(dane, n)
        end = time.time()
        print("Nazwa pliku: ", pliki[j])
        print("Wynik nieposortowany:", wynik)
        print("Czas: ", (end - start) * 1000, " ms")
        #print(kolejnosc(dane))
        dane.sort(key=lambda x: x[2])
        start1 = time.time()
        wynik = calculate(dane, n)
        end1 = time.time()
        print("")
        print("Wynik posortowany:", wynik)
        print("kolejność: ", kolejnosc(dane))
        print("Czas: ", (end1 - start1) * 1000, " ms")
        print("---")



def zad2(pliki):
    for i in range(0, len(pliki)):
        dane = pobierz_dane(pliki[i])
        n = dane[0][0]
        r = dane[0][1]
        dane = list(dane[1:n + 1])
        start = time.time()
        wynik = permut(dane, n)
        end = time.time()
        print("Nazwa pliku: ", pliki[i])

        print("BF Iteracyjnie wynik: ", wynik)
        print("Czas: ", (end - start) * 1000, " ms")

        start1 = time.time()
        #wynik = dynamicW(dane)
        wynik = BF(dane)
        end1 = time.time()
        print("")
        print("BF Rekurencyjnie wynik: ", wynik)
        print("Czas: ", (end - start) * 1000, " ms")




pliki = ["data10.txt", "data11.txt", "data12.txt", "data13.txt", "data14.txt", "data15.txt", "data16.txt", "data17.txt", "data18.txt", "data19.txt", "data20.txt"]
zad2(pliki)
