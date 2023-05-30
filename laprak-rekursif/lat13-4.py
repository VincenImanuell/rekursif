def jumlah_digit(n):
    total = 0
    for i in str(n):
        total = total + int(i)
    return total

print(jumlah_digit(182771))

def jumlah_digit_rek(n):
    if n < 10:
        return n
    else:
        return n%10+jumlah_digit_rek(n//10)
    
print(jumlah_digit_rek(182177))