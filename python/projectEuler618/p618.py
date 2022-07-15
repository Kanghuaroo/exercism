
def fib(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def findPrimeFactors(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes

def findPrimeFactorInterval(curr, prev):
    p = list()
    for i in primes:
        if i < prev - 1 or i == curr - 1 or i == prev:
            continue
        elif i > curr:
            break
        else:
            p.append(i)
    return p

def S(seqNum):
    nums = set()
    curr = fibs[seqNum]

    #get old primes
    prev1 = seen.get(fibs[seqNum-1])
    prev2 = seen.get(fibs[seqNum-2])
    for i in prev1:
        for j in prev2:
            nums.add(i*j)

    #get new primes
    if fibs[seqNum] % 2 == 0:
        nums = nums.union(findPrimeFactorSum(curr, 2))
    for p in findPrimeFactorInterval(curr, fibs[seqNum-1]):
        if p == curr:
            nums.add(p)
        else:
            nums = nums.union(findPrimeFactorSum(curr, p))
            #temp = findPrimeFactorSum(curr, p)
            #print(temp)
            #nums = nums.union(temp)
    
    seen[fibs[seqNum]] = nums
    return sum(nums)

def findEvenPrimeFactorSum(num):
    #find the pfs of an even number
    #sub 2 then highest prime
    pass

def findPrimeFactorSum(num, p):
    primeFactorSums = set()
    output = set()
    n = num - p

    if n < 0:
        return {0}
    elif n == 0:
        return {p}
    elif n in seen:
        primeFactorSums = seen.get(n)
    else:
        for prime in primes:
            if prime > n:
                break
            else:
                primeFactorSums = primeFactorSums.union(findPrimeFactorSum(n, prime))
    
    for pfs in primeFactorSums:
        output.add(p*pfs)
    
    return output

def main():
    for i in range(12):
        fibs.append(fib(i))
    #set global var
    findPrimeFactors(fibs[-1])
    

    
    print(S(5))
    print(S(6))
    print(S(7))
    print(S(8))   # should be 25681
    #print(S(9)) 
    print(fibs[8])
    
    print()
    nums = set()
    print(seen[21])
    prev1 = seen.get(fibs[8-1])
    prev2 = seen.get(fibs[8-2])
    for i in prev1:
        for j in prev2:
            nums.add(i*j)
    print(nums)
    print(seen[21].difference(nums))

primes = list()
fibs = list()
seen = dict()
seen[0] = {1}
seen[1] = {0}
seen[2] = {2}
seen[3] = {3}
seen[5] = {5,6}
seen[8] = {15,16,18}
if __name__ == "__main__":
    main()
