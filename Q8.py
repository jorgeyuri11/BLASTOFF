def checkPrimeNumber (x):
    for i in range(2,x):
        if x % i == 0:
            print ("O número não é primo.")
            break
    else:
        print ("O número é primo.")

checkPrimeNumber(10)