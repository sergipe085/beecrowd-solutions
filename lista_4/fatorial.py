def Fatorial(N):
    if N <= 1:
        return N

    return N * Fatorial(N - 1)

def divisivel(N, i):
    if (N % i == 0):
        print(i)

    if (i < N):
        divisivel(N, i + 1)

N = int(input())
divisivel(N, 1)