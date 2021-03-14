from sys import stdin
import time

num_inputs = int(input())


def readln():
    return stdin.readline().rstrip()


num = [int(i) for i in readln().split()]


def solucao_A(array_num):
    maximo = 0
    for i in range(num_inputs):
        for j in range(num_inputs):
            if i != j and array_num[i] + array_num[j] > maximo:
                maximo = array_num[i] + array_num[j]
    return maximo


tic = time.time()
print(solucao_A(num))
toc = time.time()
tempo = toc - tic
print(f"Tempo: {tempo}")
