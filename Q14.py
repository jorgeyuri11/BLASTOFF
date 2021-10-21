def isPalindrome(x):
    if x == x[::-1]:
        print("A palavra é palíndromo!")
    else:
        print("A palavra não é palíndromo!")

isPalindrome("arara")