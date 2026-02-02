def encrypt(txt, a, b):
    res = ""
    for i in txt:
        o = ord(i)
        if 65 <= o <= 90:
            x = o - 65
            res += chr((a * x + b) % 26 + 65)

        elif 97 <= o <= 122:
            x = o - 97
            res += chr((a * x + b) % 26 + 97)

        else:
            res += i

    return res

def decrypt(cip, a, b):
    res = ""
    a_inv = pow(a, -1, 26)

    for i in cip:
        o = ord(i)

        if 65 <= o <= 90:
            x = o - 65
            res += chr((a_inv * (x - b)) % 26 + 65)

        elif 97 <= o <= 122:
            x = o - 97
            res += chr((a_inv * (x - b)) % 26 + 97)

        else:
            res += i

    return res

print(encrypt("Murad elini stola vurdu, stol da qirildi, eli de", 5, 8))
print(decrypt("Qepix clwvw uzali jepxe, uzal xi kwpwlxw, clw xc", 5, 8))