for i in range(100):
    j,k,l=i%3,i%5,i
    if j==0 and k==0:
        l='FizzBuzz'
    elif j==0: 
        l='Buzz'
    elif k==0:
        l='Fizz'
    print(l)
