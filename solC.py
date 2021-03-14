from sys import stdin
import time

num_inputs = int(input())


def readln():
    return stdin.readline().rstrip()


num = [int(i) for i in readln().split()]


def solucao_C(array_num):
    max1 = 0
    max2 = 0
    for elemento in array_num:
        if elemento > max2:
            max2 = elemento
        if elemento > max1:
            max2 = max1
            max1 = elemento
    return max1 + max2


tic = time.time()
print(solucao_C(num))
toc = time.time()
tempo = toc - tic
print(f"Tempo: {tempo}")
