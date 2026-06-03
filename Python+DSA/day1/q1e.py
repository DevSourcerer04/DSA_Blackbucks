def is_prime(n, i=2):
    if n < 2:
        return False

    if i * i > n:
        return True

    if n % i == 0:
        return False

    return is_prime(n, i + 1)


def find_primes(start, end, primes):
    if start > end:
        return primes

    if is_prime(start):
        primes.append(start)

    return find_primes(start + 1, end, primes)


start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = find_primes(start, end, [])

print("Prime numbers:", primes)
print("Count:", len(primes))
