def isprime(n):
    if n == 1:
        return False
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count +=1
        if count>2:
            return False
    return True

number = -1

while number != 0:
    number = int(input())
    if(number == 0):
        break
    if(isprime(number)):
        print(number,"é primo")
    else:
        print(number,"não é primo")