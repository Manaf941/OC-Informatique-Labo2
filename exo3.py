

numbers = []

# loop over every number between 2 and 300 (incl.)
for num in range(2, 300 + 1):
    is_prime = True

    # verify it is not divisible by any other prime number
    # we encountered before
    for prime in numbers:
        # if it is divisible, n % p will equal 0
        if num % prime == 0:
            is_prime = False
            break
    
    if is_prime:
        numbers.append(num)

# print the numbers
print(", ".join([str(x) for x in numbers]))