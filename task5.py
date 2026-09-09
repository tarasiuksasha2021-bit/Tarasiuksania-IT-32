name = "Sasha"
surname = "Tarasiuk"
group = "IT-32"

d = 7
c = 8

print(f"{name} {surname}, {group}")

n = d * c

print(f"n = {d} * {c} = {n}")

# Divisors

divisors = []
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisors_sum += i

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")

# Prime check

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

# All prime numbers from 2 to n

primes = []

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        primes.append(number)

print("Primes up to", n, ":", *primes)
print(f"Primes count: {len(primes)}")