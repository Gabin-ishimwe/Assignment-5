# we are going to implement an algorithm the calculates
# the sum of k largest numbers in the list

def sum(arr, k):
    nonDuplicate = set(arr)
    setBack = list(nonDuplicate)
    setBack.sort(reverse=True)
    print(setBack)
    suming = 0
    for i in range(k):
        suming += setBack[i]
    print(suming)

sum([1, 6, 7, 2, 3, 3], 3)