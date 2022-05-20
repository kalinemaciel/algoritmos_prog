def testarepetidos(vet):
    for i in range(0, len(vet)-1):
        for j in range(i+1, len(vet)):
            if vet[i] == vet[j]:
                return True
    return False

arr = [1,2,3,4,6,7,8,9,0,0]
arr2 = [1,2,3]

print(testarepetidos(arr))
print(testarepetidos(arr2))