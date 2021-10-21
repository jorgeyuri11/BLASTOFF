A = [1, 2, 3, 4]
B = [1, 2, 5, 8]

def listIntersection(x,y):
    C = [i for i in x if i in y]
    print(C)

listIntersection(A, B)
