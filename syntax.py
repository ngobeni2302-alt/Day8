# 1. Write a function print_odds_reverse(n) that prints only odd numbers from n down to 1 using a for
# loop.
def print_odds_reverse(n):
    for i in range(n, 1,-1):
        if i % 2 != 0:
            print (i)
    



# 2. Write a function count_multiples(n, k) that prints all numbers from 1 to n that are divisible by k.
def count_multiples(n, k):
    for i in range(1,n+1):
        if i % k == 0:
            print(i)


# 3. Write a function print_triangle(n) that prints a right-angled triangle of stars up to n rows using loops and string multiplication.
def print_triangle(n):
    for i in range(1,n+1):
            print("*" *i )

    


# 4. Write a function print_number_triangle(n) that prints a number pattern where each row contains numbers from 1 up to the row number.
def print_number_triangle(n):
    for i in range(1,n+1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
print_number_triangle(5)     
          



# 5. Write a function sum_until_limit(limit) that keeps adding consecutive numbers starting from 1 until the total is greater than or equal to limit. Print the final total.
def sum_until_limit(limit):
    sum = 0
    for i in range(1, limit):
        if sum != limit:
            final_total = sum + i
    print(final_total)
sum_until_limit(10)        

# 6. Write a function factorial(n) using a loop (no recursion allowed).
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 7. Write a function count_digits(number) that counts how many digits are in a positive integer using a loop.
def count_digits(number):
    


# 8. Write a function reverse_number(n) that reverses a number using loops (e.g., 1234 → 4321).



# 9. Write a function multiplication_table(n) that prints the multiplication table of n from 1 to 10 using a loop.



# 10. Write a function print_pyramid(n) that prints a centered pyramid pattern of stars with n levels using nested loops.