start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = []

if end >= 2:
    is_prime = [True] * (end + 1)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, int(end ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, end + 1, num):
                is_prime[multiple] = False

    for num in range(max(2, start), end + 1):
        if is_prime[num]:
            primes.append(num)

print("Prime numbers:", primes)
print("Count:", len(primes))
