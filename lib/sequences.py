#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []

    if length == 0:
        print(sequence)
        return
    
    elif length == 1:
        sequence = [0]
        print(sequence)
        return
    
    sequence = [0, 1]
    while len(sequence) < length:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    print(sequence)    
    pass

# def print_fibonacci(n):
#     if n <= 0:
#         print([])
#         return

#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])

#     print(fib[:n])
