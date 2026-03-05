# AERT - Algorithmic Efficiency & Recursion Toolkit
# Name: Chirag Satbir Yadav
# Roll No: 2501730067
# Course: B.Tech CSE (AI Ml), 2nd Semester
# Data Structures (ETCCDS202)
# Name of the School:	School of Engineering & Technology 
# Program: B.Tech CSE (AI and ML) 
# Unit Title: Foundations & Algorithmic Analysis  
# Batch: 2025-26 
# Submitted To: Mrs. Neetu Chauhan


#PART A ="STACK ADT"

import sys


class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# PART B = "FACTORIAL RECURSIVE"
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#FIBONACCI NAIVE
def fibonacci(n):
    global naive_calls
    naive_calls += 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#FIBONACCI MEMOIZATION
def fibonacci_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]

#PART C = "TOWER OF HANOI"
def move_plates(n, source, destination, help, stack):
    if n == 1:
        move = f"Move plate 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    move_plates(n - 1, source, help, destination, stack)

    move = f"Move plate {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    move_plates(n - 1, help, destination, source, stack)


#PART D = "Recursive Binary Search"
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1) 
    else:
        return binary_search(arr, target, mid + 1, high) 
    
# Main function to test all implementations
def main():
    print("Factorial Tests:")
    for n in [2, 3, 6, 11]:
        print(f"Factorial({n}) = {factorial(n)}")

    print("\nFibonacci Tests:")
    for n in [5, 15, 25, 30]:
        global naive_calls, memo_calls
        naive_calls = 0
        result_naive = fibonacci(n)
        print(f"\nNaive Fibonacci({n}) = {result_naive}")
        print("Naive Calls =", naive_calls)
        memo_calls = 0
        result_memo = fibonacci_memo(n, {})
        print(f"Memoized Fibonacci({n}) = {result_memo}")
        print("Memo Calls =", memo_calls)

    print("\nTower of Hanoi Tests:")
    stack = StackADT()
    move_plates(3, 'A', 'B', 'C', stack)
    print("\nTotal Moves Stored in Stack:", stack.size())

    print("\nBinary Search Tests:")
    arr = [1,3,5,7,9,11,13]
    for key in [7, 1, 13, 2]:
        index = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> Index: {index}")
    empty_arr = []
    print("Search in empty array:", binary_search(empty_arr, 5, 0, -1))

if __name__ == "__main__":
    file = open("output.txt", "w")
    sys.stdout = file 
    main()
    file.close()