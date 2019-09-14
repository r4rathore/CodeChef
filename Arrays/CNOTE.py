#Chef likes to write poetry. Today, he has decided to write a X pages long poetry, but unfortunately his notebook has only Y pages left in it. Thus he decided to buy a new CHEFMATE notebook and went to the stationary shop. Shopkeeper showed him some N notebooks, where the number of pages and price of the ith one are Pi pages and Ci rubles respectively. Chef has spent some money preparing for Ksen's birthday, and then he has only K rubles left for now.
#Chef wants to buy a single notebook such that the price of the notebook should not exceed his budget and he is able to complete his poetry.
#Help Chef accomplishing this task. You just need to tell him whether he can buy such a notebook or not. Note that Chef can use all of the Y pages in the current notebook, and Chef can buy only one notebook because Chef doesn't want to use many notebooks.

def cnote(targetPage, leftPage, leftAmount, n):
    PCArr = []
    for sample in range(n):
        PCArr.append(input().split(' '))

    for PC in PCArr:
        P = int(PC[0])
        C = int(PC[1])
        if((P >= 1 & P <= 10**3) & (C >= 1 & C <= 10**3)):
            if(P >= (targetPage - leftPage) & leftAmount >= C):
                return True
            continue
    return False

T = int(input())
if T >=1 & T <= 10**5:
    subTaskCriteria = 0
    resultArr = []
    for testCase in range(T):
        XYKN = input().split(' ')

        if(len(XYKN) == 4):
            X = int(XYKN[ 0 ])
            Y = int(XYKN[ 1 ])
            K = int(XYKN[ 2 ])
            N = int(XYKN[ 3 ])

            #subTaskCriteria += N
            if(subTaskCriteria == 0):
                if((X >= 1 & X <= 10**3) & (Y >= 1 & Y <= 10**3) & (K >= 1 & K <= 10**3) & (N >= 1 & N <= 10**5)):
                    resultArr.append(cnote(X,Y,K,N))

    for result in resultArr:
        if(result):
            print('LuckyChef')
        else:
            print('UnluckyChef')



