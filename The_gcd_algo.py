def find_gcd_using_euclidean_algo(num1, num2):
    if num1 > num2:
        a , b = num1, num2
    else:
        a , b = num2, num1

    while b != 0:
        r = a % b
        a = b
        b = r
    return a
print(find_gcd_using_euclidean_algo(21,98))
