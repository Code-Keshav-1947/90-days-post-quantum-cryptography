def prime_checker(n):
    if n < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    return is_prime


def prime_generator(limit):
    primes = []
    for num in range(2, limit + 1):
        if prime_checker(num):
            primes.append(num)
    return primes


def trial_division(n):
    factors = []

    if n < 2:
        return factors

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return factors


def main():
    number = int(input("Enter a number to check if it's prime: "))
    if prime_checker(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    print(f"Prime factors of {number}: {trial_division(number)}")
    wanted_limit = int(input("Enter a limit to generate prime numbers up to: "))
    print(f"Prime numbers up to {wanted_limit}: {prime_generator(wanted_limit)}")


if __name__ == "__main__":
    main()
