import random
import time

"""TESTAM SA VEDEM DACA VECTORUL E SORTAT"""


def testSort(v):
    v2 = sorted(v)
    if v == v2:
        return "Sortat"
    return "Nesortat"


""""MERGE SORT   O(nlog(n))"""


def interclasare(v, st, mij, dr):
    i = st
    j = mij + 1
    aux = []
    while i <= mij and j <= dr:
        if v[i] <= v[j]:
            aux.append(v[i])
            i += 1
        else:
            aux.append(v[j])
            j += 1
    aux.extend(v[i:mij + 1])
    aux.extend(v[j:dr + 1])
    v[st:dr + 1] = aux[:]


def MergeSort(v, st, dr):
    if st < dr:
        mij = (st + dr) // 2
        MergeSort(v, st, mij)
        MergeSort(v, mij + 1, dr)
        interclasare(v, st, mij, dr)
    return v


"""SHELL SORT"""


def ShellSort(v):
    interval = len(v) // 2
    while interval > 0:
        for i in range(interval, len(v)):
            temp = v[i]
            j = i
            while j >= interval and v[j - interval] > temp:
                v[j] = v[j - interval]
                j -= interval

            v[j] = temp
        interval //= 2
    return v


"""COUNT SORT"""


def CountSort(v):
    n = len(v)
    if n <= 1:
        return v
    mx = max(v)
    count = [0] * (mx + 1)

    for nr in v:
        count[nr] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]  # aflam pozitia pe care s ar afla numarul in vectorul sortat
    output = [0] * n
    for val in reversed(v):
        index = count[val] - 1
        output[index] = val
        count[val] -= 1

    return output


"""RADIX SORT"""
"""
def RadixSort10(v):
    mx=max(v)
    p=1
    while mx/p>=1:
        vnou=[]
        M=[[] for i in range(10)]
        for i in range(len(v)):
            M[v[i]//p%10].append(v[i])
        for i in range(10):
            for j in range(len(M[i])):
                vnou.append(M[i][j])
        v=vnou
        p*=10"""

"""RADIX SORT 2^4 2^8 2^12 2^16---- CU CAT NUMARUL ELEMENTELOR DIN VECTOR ESTE MAI MARE TIMPII DE RULARE SCAD(CEL
MAI MULT DUREAZA ALGORITMUL IN BAZA 2^8 APOI CEL IN BAZA 2^16 DEOARECE )"""


def radix_sort4(v):
    max_element = max(v)
    max_digit = (max_element.bit_length() + 3) // 4
    mask = 2 ** 4 - 1
    for digit in range(max_digit):
        buckets = [[] for _ in range(2 ** 4)]

        for nr in v:
            digit_val = (nr >> (digit * 4)) & mask
            buckets[digit_val].append(nr)

        v = [nr for bucket in buckets for nr in bucket]

    return v


def radix_sort8(v):
    max_element = max(v)
    max_digit = (max_element.bit_length() + 7) // 8
    mask = 2 ** 8 - 1
    for digit in range(max_digit):
        buckets = [[] for _ in range(2 ** 8)]

        for nr in v:
            digit_val = (nr >> (digit * 8)) & mask
            buckets[digit_val].append(nr)

        v = [nr for bucket in buckets for nr in bucket]

    return v


def radix_sort12(v):
    max_element = max(v)
    max_digit = (max_element.bit_length() + 11) // 12
    mask = 2 ** 12 - 1
    for digit in range(max_digit):
        buckets = [[] for _ in range(2 ** 12)]

        for nr in v:
            digit_val = (nr >> (digit * 12)) & mask
            buckets[digit_val].append(nr)

        v = [nr for bucket in buckets for nr in bucket]

    return v


def radix_sort16(v):
    max_element = max(v)
    max_digit = (max_element.bit_length() + 15) // 16
    mask = 2 ** 16 - 1
    for digit in range(max_digit):
        buckets = [[] for _ in range(2 ** 16)]

        for nr in v:
            digit_val = (nr >> (digit * 16)) & mask
            buckets[digit_val].append(nr)

        v = [nr for bucket in buckets for nr in bucket]

    return v


"""BUBBLE SORT"""


def BubbleSort(v):
    for i in range(len(v)):
        swapped = False
        for j in range(0, len(v) - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                swapped = True
        if not swapped:
            break
    return v


"""Aflam timpii de rulare pentru fiecare metoda de sortare"""
f = open("input.txt", "r")
g = open("output.txt", "w")
teste = int(f.readline())
sortari = ["MergeSort", "ShellSort", "CountSort", "BubbleSort", "radix_sort4", "radix_sort8", "radix_sort12",
           "radix_sort16"]
for test in range(teste):
    L = f.readline().split()
    n = int(L[0])
    maxim = int(L[1])
    print("Timpii de rulare pentru testul {0}, unde numarul de elemente este {1}, iar elementul maxim este {2}".format(
        test + 1, n, maxim))
    Vector = [random.randint(0, maxim) for i in range(n)]
    for sort in sortari:
        if sort == "MergeSort":
            v = [Vector[i] for i in range(len(Vector))]
            time_start = time.time()
            v = MergeSort(v, 0, n - 1)
            time_stop = time.time()
            print("Time for Merge Sort:   {0}".format(time_stop - time_start), testSort(v))
        if sort == "ShellSort":
            if n <= 10 ** 7:
                time_start = time.time()
                v = ShellSort(v)
                time_stop = time.time()
                print("Time for Shell Sort:   {0}".format(time_stop - time_start), testSort(v))
            else:
                print("Algoritmul nu poate rula in timp util.")
        if sort == "CountSort":
            if maxim <= 10 ** 8:
                v = [Vector[i] for i in range(len(Vector))]
                time_start = time.time()
                v = CountSort(v)
                time_stop = time.time()
                print("Time for Count Sort:   {0}".format(time_stop - time_start), testSort(v))
            else:
                print("Nu exista memorie suficienta pentru a fi rulat algoritmul de numarare")

        if sort == "radix_sort4":
            v = [Vector[i] for i in range(len(Vector))]
            time_start = time.time()
            v = radix_sort4(v)
            time_stop = time.time()
            print("Time for RADIX SORT 4:   {0}".format(time_stop - time_start), testSort(v))
        if sort == "radix_sort8":
            v = [Vector[i] for i in range(len(Vector))]
            time_start = time.time()
            v = radix_sort8(v)
            time_stop = time.time()
            print("Time for RADIX SORT 8:   {0}".format(time_stop - time_start), testSort(v))
        if sort == "radix_sort12":
            v = [Vector[i] for i in range(len(Vector))]
            time_start = time.time()
            v = radix_sort12(v)
            time_stop = time.time()
            print("Time for RADIX SORT 12:   {0}".format(time_stop - time_start), testSort(v))
        if sort == "radix_sort16":
            v = [Vector[i] for i in range(len(Vector))]
            time_start = time.time()
            v = radix_sort16(v)
            time_stop = time.time()
            print("Time for RADIX SORT 16:   {0}".format(time_stop - time_start), testSort(v))
        if sort == "BubbleSort":
            if n < 10 ** 5:
                v = [Vector[i] for i in range(len(Vector))]
                time_start = time.time()
                v = BubbleSort(v)
                time_stop = time.time()
                print("Time for BUBBLE SORT :   {0}".format(time_stop - time_start), testSort(v))

            else:
                print("Lista nu poate fi sortata intr-un timp util")
    time_start = time.time()
    v = [Vector[i] for i in range(len(Vector))]
    v = sorted(v)
    time_stop = time.time()
    print("Time for Python function for sorting lists:   {0}".format(time_stop - time_start), testSort(v) + "\n")

