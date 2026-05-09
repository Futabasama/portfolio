def pgcd_recursif(a, b):
    if b == 0:
        return a
    else:
        return pgcd_recursif(b, a % b)
# Tests
print(f"pgcd_recursif(48, 18) = {pgcd_recursif(48, 18)}")
print(f"pgcd_recursif(100, 35) = {pgcd_recursif(100, 35)}")
print(f"pgcd_recursif(7, 5) = {pgcd_recursif(7, 5)}")
