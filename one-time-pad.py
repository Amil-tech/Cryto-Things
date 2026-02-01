from random import randint

def bin_to_dec(b):
    uzun = len(b)
    res = 0
    for i in b:
        res += (1 << (uzun - 1)) * int(i)
        uzun -= 1
    return res

def dec_to_bin(d):
    res = ""
    while d != 0:
        q = d & 1
        res = str(q) + res
        d = d >> 1
    return res

def plain_to_binary(txt):
    res = ""
    for ch in txt:
        b = bin(ord(ch))[2:]
        res += '0' * (8 - len(b)) + b
    return res

def binary_to_plain(b):
    res = ""
    for i in range(0, len(b), 8):
        elem = chr(bin_to_dec(b[i:i+8]))
        res += elem
    return res

def generate_key(l):
    res = ""
    for _ in range(l):
        res += str(randint(0,1))
    return res

def encrypt(k, m):
    res = ""
    for i in range(len(k)):
        # xor = (int(k[i]) + int(m[i])) % 2
        xor = int(k[i]) ^ int(m[i])
        res += str(xor)
    return res

def decrypt(k, c):
    return encrypt(k, c)

text = input("Enter the text: ")
message = plain_to_binary(text)
key = generate_key(len(message))
cipher_txt_bits = encrypt(key, message)
decrypted_txt_bits = decrypt(key, cipher_txt_bits)
decrypted_txt = binary_to_plain(decrypted_txt_bits)

print("Message: " + message)
print("Key: " + key)
print("Encrypted in bits: " + cipher_txt_bits)
print("Decrypted in bits: " + decrypted_txt_bits)
print("Decrypted message: " + decrypted_txt)

