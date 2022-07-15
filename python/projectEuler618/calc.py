def five():
    sum = 0
    sum += 5
    sum += 3*2
    print(sum)

def eight():
    sum = 0
    sum += 5*3
    sum += 3*3*2
    sum += 2*2*2*2
    print(sum)

def thirteen():
    sum = 0
    #old primes
    sum += 5*5*3
    sum += 5*3*3*2
    sum += 5*2*2*2*2
    sum += 3*3*3*2*2
    sum += 3*2*2*2*2*2

    #new primes
    sum += 13
    sum += 11*2
    sum += 7*2*2*2
    sum += 7*3*3

    print(sum)

five()
eight()
thirteen()

print()
sum = 0
sum += 13
sum += 11*2
sum += 7*2*2*2
sum += 7*3*3
print(sum)
