def contamultiplos(n1, n2, n3):                                      
    count = 0
    for i in range(n1, n2):                                                 
        if i%n3 == 0:
            count += 1
    return count

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(contamultiplos(n1, n2, n3))