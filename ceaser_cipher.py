def encrypt(txt, k):
    res = ""
    k %= 26
    for i in txt:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
            next_loc = ord(i) + k
            if (65 <= ord(i) <= 90 < next_loc) or (97 <= ord(i) <= 122 < next_loc):
                next_loc -= 26
            res += chr(next_loc)
        else:
            res += i
    return res

def decrypt(cip, k):
    res = ""
    k %= 26
    for i in cip:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
            next_loc = ord(i) - k
            if (next_loc < 65 <= ord(i) <= 90) or (next_loc < 97 <= ord(i) <= 122):
                next_loc += 26
            res += chr(next_loc)
        else:
            res += i
    return res

print(encrypt("Murad elini stola vurdu, stol dozmedi", -43)) # Vdajm nurwr bcxuj edamd, bcxu mxivnmr
print(decrypt("Vdajm nurwr bcxuj edamd, bcxu mxivnmr", -43))