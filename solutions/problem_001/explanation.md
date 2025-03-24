## Multiples of 3 or 5

[EULER 001](https://www.hackerrank.com/contests/projecteuler/challenges/euler001)

### Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

### Problem Analysis

The problem asks for the sum of all the multiples of 3 or 5 below a given number. We can solve this problem by iterating over all the numbers below the given number and checking if the number is divisible by 3 or 5. If it is, we add it to the sum.

### Plan

1. Initialize a variable `sum` to store the sum of multiples of 3 or 5.
2. Iterate over all the numbers below the given number.
3. For each number, check if it is divisible by 3 or 5.
4. If it is, add the number to the sum.
5. Return the sum as the final result.

### Solution

#### Attempt 1

I use brute force to iterate over all the numbers below the given number and check if the number is divisible by 3 or 5. If it is, I add it to the sum.

This approach is simple and straightforward, but it may not be efficient for large numbers.

```python
## Imperative Approach
def multiples_of_3_and_5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

## Inline Approach
def multiples_of_3_and_5(n):
    return sum(for x in range(n) if x % 3 == 0 or x % 5 == 0)
```

> Terminated due to timeout :(

#### Attempt 2

I optimize the solution by calculating the sum of multiples of 3 and 5 separately and then subtracting the sum of multiples of 15 (since they are counted twice).

This approach reduces the number of iterations and improves the efficiency of the solution.

Arithmetic Progression:

> An Arithmetic Progression (AP) is a sequence where each term increases by a fixed amount (common difference).

Sum or terms of an arithmetic progression:

> Sn = n /2 \* (a1 + an)

Minimum Multiple Common to 3 and 5 is 15.

```python
def multiples_of_3_and_5(n):
    n -= 1
    sum_3 = 3 * (n // 3) * (n // 3 + 1) // 2
    sum_5 = 5 * (n // 5) * (n // 5 + 1) // 2
    sum_15 = 15 * (n // 15) * (n // 15 + 1) // 2
    return sum_3 + sum_5 - sum_15
```

### Test Cases

- multiples_of_3_and_5(1000) -> 233168
- multiples_of_3_and_5(10) -> 23
- multiples_of_3_and_5(49) -> 543

### Complexity Analysis

The time complexity for this solution is O(1). We not iterate over all the numbers below the given number to find the sum of multiples of 3 or 5. Using Sum of arithmetic progression to solve without iterate each number.

The space complexity for this solution is O(1), as we only use a constant amount of extra space to store the sum.
