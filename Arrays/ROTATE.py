#Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
def rotate(arr : list, n):
    for i in range(n):
        firstelement = arr[0]
        arr.pop(0)
        arr.append(firstelement)
    return arr

T = int(input())
if T >= 1 & T <= 200:
    result = []
    for testCases in range(T):
        ND = input().split(' ')
        N = int(ND[0])
        D = int(ND[1])

        if (N >= 1 & N <= 10**7) & (D >= 1 & D <= N):
            arr = []
            str_array = input().split(' ')
            try:
                arr = list(map(int, str_array))
            except:
                arr = list(map(int, str_array[:-1]))

            result.append(rotate(arr, D))

    for res in result:
        print(res)