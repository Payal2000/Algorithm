#Master Theorm in python

import math

def main():
    print("This program calculates the master theorm")
    print("for a given function of n")
    print("f(n) = a(n) * f(n/b) + f(n%b) + O(n^d)")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    d = int(input("Enter d: "))
    n = int(input("Enter n: "))
    if a == 0:
        print("The master theorm is not applicable")
    elif a == 1:
        if b == 1:
            print("The master theorm is not applicable")
        else:
            print("The master theorm is applicable")
            print("The time complexity is O(n^d)")
    elif a > 1:
        if b == 1:
            print("The master theorm is applicable")
            print("The time complexity is O(n^d * log(n))")
        elif b > 1:
            if a < b**d:
                print("The master theorm is applicable")
                print("The time complexity is O(n^d * log(n))")
            elif a == b**d:
                print("The master theorm is applicable")
                print("The time complexity is O(n^d)")
            elif a > b**d:
                print("The master theorm is applicable")
                print("The time complexity is O(n^d * log(n))")
        else:
            print("The master theorm is not applicable")
    else:
        print("The master theorm is not applicable")

if __name__ == "__main__":
    main()

