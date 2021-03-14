from sys import stdin
import time

num_inputs = int(input())


def readln():
    return stdin.readline().rstrip()


num = [int(i) for i in readln().split()]


def solucao_B(array_num):
    array_num.sort(reverse=True)
    return array_num[0] + array_num[1]


tic = time.time()
print(solucao_B(num))
toc = time.time()
tempo = toc - tic
print(f"Tempo: {tempo}")
