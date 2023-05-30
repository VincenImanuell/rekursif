import timeit

def fibo(n):
    f1,f2=1,1
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
    return fib

def fibo_rekursif_upgrade(n, list_fibo):
    if n == 1 or n == 2:
        return 1
    else:
        if list_fibo[n-1] != 0:
            return list_fibo[n-1]
        else:
            list_fibo[n-1] = fibo_rekursif_upgrade(n-1, list_fibo) + fibo_rekursif_upgrade(n-2, list_fibo)
            return fibo_rekursif_upgrade(n-1, list_fibo) + fibo_rekursif_upgrade(n-2, list_fibo)

start = timeit.default_timer()
hasil = fibo(40)
end = timeit.default_timer()
waktu = (end-start)
print(f'Waktu: {waktu} detik.')

n = 20
list_fibo = [0] * n
start = timeit.default_timer()
hasil = fibo_rekursif_upgrade(n, list_fibo)
end = timeit.default_timer()
waktu2 = (end-start)
print(f'Waktu2: {waktu2} detik.')