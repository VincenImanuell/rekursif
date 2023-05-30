def palindrome(kalimat):
    kalimat_balik = kalimat[::-1]
    if kalimat == kalimat_balik:
        return True
    else:
        return False

print(palindrome('kasur rusak'))
print(palindrome('duta wacana'))


def palindrome_rek(kalimat, depan, belakang):
    if depan == belakang: # base case ketika tinggal 1 karakter
        return True
    elif depan == belakang - 1:
        if kalimat[depan] == kalimat[belakang]:
            return True
        else:
            return False
    # recursive case
    if kalimat[depan] == kalimat[belakang]:
        return palindrome_rek(kalimat, depan+1, belakang-1)
    else:
        return False
    
print(palindrome_rek('kasur rusak', 0, (len('kasur rusak'))-1))
print(palindrome_rek('duta wacana', 0, (len('duta wacana'))-1))

# laprak: soal 1, 3, 4 dari ppt alpro