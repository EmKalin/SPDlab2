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

globalDictionary = {}

globalDic = {}

def iteracja(dane):
    for i in range (1, 2**len(dane)):
        #n = len(tab)
        zupa = bin(i)[2:]
        #print(zupa)
        zupa1 = len(dane) - len(zupa)
        laczny = "0"*zupa1
        tablica = [laczny,zupa]
        template_string = "".join(tablica)
        #print(template_string)



        C = 0
        n = len(template_string) - 1
        for i in range(0, len(template_string)):
            if template_string[i] == "1":
                C = C + dane[n - i][0]

        fin = []

        if template_string.count('1') == 1:
            x = template_string.index('1')
            K = dane[n - x][1] * max(dane[n - x][0] - dane[n - x][2], 0)
            globalDic[template_string] = K
            # print(globalDic)
            #return globalDic[template_string]

        else:
            for i in range(0, len(template_string)):
                # n = len(template_string)-1
                temp_string = copy.deepcopy(template_string)
                temp_list = []
                temp_list = list(temp_string)
                # print(temp_string)

                if temp_list[i] == '1':
                    temp_list[i] = '0'
                    ret_str = "".join(temp_list)
                    K = dane[n - i][1] * max(C - dane[n - i][2], 0)
                    #print(ret_str)

                    add = globalDic[ret_str] + K

                    fin.append(add)

            globalDic[template_string] = min(fin)
        #print(globalDic[template_string])
    #print(globalDic)
    return globalDic[bin(2**len(dane)-1)[2:]]



def dynamicWRec(template_string,dane):

    if not  template_string in globalDictionary:
        C = 0
        n=len(template_string)-1
        for i in range(0, len(template_string)):
            if template_string[i] == "1":
                C = C + dane[n-i][0]

        fin = []
        if template_string.count('1') == 1:

            x = template_string.index('1')
            K = dane[n - x][1] * max(dane[n - x][0] - dane[n - x][2], 0)
            globalDictionary[template_string] = K
            #print(globalDictionary)
            return globalDictionary[template_string]

        else:

            for i in range(0,len(template_string)):
                #n = len(template_string)-1
                temp_string = copy.deepcopy(template_string)
                temp_list = []
                temp_list = list(temp_string)
                #print(temp_string)

                if temp_list[i] == '1':
                    temp_list[i] = '0'
                    ret_str = "".join(temp_list)
                    K = dane[n-i][1] * max(C - dane[n-i][2], 0)
                        #print(K)
                        #print("----------------------------")
                    # if temp_list.count('1') == 1:
                    #     x = temp_list.index('1')
                    #     K = dane[n-x][1]*max(dane[n-x][0]-dane[n-x][2],0)
                    #     globalDictionary[ret_str] = K
                    #     fin.append(K)
                    #else:
                    ent = dynamicWRec(ret_str, dane) + K
                        #fin.append(globalDictionary[ret_str])
                        #globalDictionary[ret_str] = temp
                    fin.append(ent)
            globalDictionary[template_string] = min(fin)
            return globalDictionary[template_string]
    else:
        return globalDictionary[template_string]

def zad1(pliki):
    for j in range(0, len(pliki)):
        dane = pobierz_dane(pliki[j])
        n = dane[0][0]
        r = dane[0][1]
        dane = list(dane[1:n + 1])
        str = ("1")*len(dane)
        start = time.time()
        wynik = dynamicWRec(str, dane)
        end = time.time()
        print("Nazwa pliku: ", pliki[j])
        print("Wynik :", wynik)
        print("Czas: ", (end - start) * 1000, " ms")
        #print(globalDictionary)
        print("-------------------")


def zad2(pliki):
    for j in range(0, len(pliki)):
        dane = pobierz_dane(pliki[j])
        n = dane[0][0]
        r = dane[0][1]
        dane = list(dane[1:n + 1])
        #str = ("1")*len(dane)
        start = time.time()
        wynik = iteracja(dane)
        end = time.time()
        print("Nazwa pliku: ", pliki[j])
        print("Wynik :", wynik)
        print("Czas: ", (end - start) * 1000, " ms")
        #print(globalDic)
        print("-------------------")

pliki = ["data10.txt", "data11.txt", "data12.txt", "data13.txt", "data14.txt", "data15.txt", "data16.txt", "data17.txt", "data18.txt", "data19.txt", "data20.txt"]
zad2(pliki)