def factorial (x):
    result = 1
    for i in range(1, x+1):
        result *= i
    print ("O fatorial deste número é: ", result)

factorial(7)
