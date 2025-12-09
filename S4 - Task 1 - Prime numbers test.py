def is_prime(n):
    if n <= 1:
        print ('Not Prime')
        return
    if n == 2:
        print ('Prime')
        return
    if n % 2 == 0:
        print ('Not Prime')
        return
    for i in range (2, n):
        if n%i == 0:
            print ('Not Prime')
            return
    print ('Prime')


n = int(input('Please enter your number : '))
is_prime(n)

