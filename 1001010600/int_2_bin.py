def mybin(x):
    print('__name__={}'.format(__name__))
    #entero a binario
    r = x%2
    x=x//2 
    b = str(r)

    while x >= 2 :
        r = x%2
        x=x//2 
        b = str(r) + b
    b = str(x)+b
    #================
    return b.rjust(8, '0')

if __name__ == '__main__':
    n=input('Escriba un entero:\n')
    b = mybin(int(n))
   
    print('Su representación binaria es: {}'.format(b))