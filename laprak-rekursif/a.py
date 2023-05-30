import timeit
import sys

sys.setrecursionlimit(100000)

# hello world perulangan
def helloworld_perulangan(n):
    urutan = 1
    for i in range(n):
        print(urutan, 'Hello world!')
        urutan += 1

# hello world rekursif
def helloworld_rekursif(n, x):
    if n == 0: # base case
        return # fungsi selesai
    else:
        print(x, 'Hello world!')
        helloworld_rekursif(n-1, x+1) # print sisanya


start = timeit.default_timer()
helloworld_perulangan(100)
end = timeit.default_timer()
print(f'Waktu yang diperlukan: {(end-start)/1000} ms.')

print('\n\n')

start = timeit.default_timer()
helloworld_rekursif(2000, 1)
end = timeit.default_timer()
print(f'Waktu yang diperlukan: {(end-start)/1000} ms.')