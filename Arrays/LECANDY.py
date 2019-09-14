#All submissions for this problem are available.
#A Little Elephant and his friends from the Zoo of Lviv like candies very much.
#There are N elephants in the Zoo. The elephant with number K (1 ≤ K ≤ N) will be happy if he receives at least AK candies. There are C candies in all in the Zoo.
#The Zoo staff is interested in knowing whether it is possible to make all the N elephants happy by giving each elephant at least as many candies as he wants, that is, the Kth elephant should receive at least AK candies. Each candy can be given to only one elephant. Print Yes if it is possible and No otherwise.

def Algo(noe, noc, arr):
    leftCandy = noc
    for j in range(noe):
        candy = int(arr[ j ])
        if(leftCandy < candy):
            return False
        leftCandy = leftCandy - candy
    return True

T = int(input())
if T >= 1 & T <= 100:
    result = [ ]
    for x in range(T):
        NC = input().split(' ')
        N = int(NC[0])
        C = int(NC[1])

        if (N >=1 & N <= 100) & (C >= 1 & C <= 10 ** 9):
            A = input().split(' ')

            if Algo(N, C, A):
                result.append('Yes')
            else:
                result.append('No')

    for res in result:
        print(res)