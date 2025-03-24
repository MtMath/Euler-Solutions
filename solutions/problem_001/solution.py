# Brute force in O(n), iterating over all numbers
def multiples_of_3_and_5(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

# Arithmetic progression in O(1), sum of multiples of 3 and 5
def multiples_of_3_and_5(n):
    n -= 1
    sum_3 = 3 * (n // 3) * (n // 3 + 1) // 2
    sum_5 = 5 * (n // 5) * (n // 5 + 1) // 2
    sum_15 = 15 * (n // 15) * (n // 15 + 1) // 2
    return sum_3 + sum_5 - sum_15
