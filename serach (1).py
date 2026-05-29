#Jamal
#serach.py





import random

secret_number = random.randint(1, 100)
print(f"The Secret Number is: {secret_number}")


# SEARCH

def linear_search(secret):

    attempts = 0

    for guess in range(1, 101):

        attempts += 1

        if guess == secret:

            print("\n--- Linear Search ---")
            print(f"Found it! Number: {guess}")
            print(f"Attempts: {attempts}")
            break

linear_search(secret_number)



# SEARCH

def binary_search(secret):
    low = 1
    high = 100
    attempts = 0
    found = False

    while not found:
        attempts += 1
        mid = (low + high) // 2

        if mid == secret:
            found = True
            print("\n--- Binary Search ---")
            print(f"Found it! Number: {mid}")
            print(f"Attempts: {attempts}")

        elif mid < secret:
            low = mid + 1 # search higher half

        else:
            high = mid - 1 # search lower half


binary_search(secret_number)

