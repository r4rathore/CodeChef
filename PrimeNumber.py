import math
import time
# 1st solution Time Complexity O(n)
def isPrime1(n):
    for x in range(2, n):
        if(n % x == 0):
            return False
    return True

def isPrime2(n):
    limitRange = math.floor(math.sqrt(n))
    for x in range(2, limitRange):
        if(n % 2 == 0):
            return False
    return True

inp = int(input('Enter the number'))

start_time = time.time()
print('start time ' + str(start_time))
print(isPrime2(inp))
print('end time ' +str((time.time() - start_time)))
