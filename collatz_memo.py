import time
import matplotlib.pyplot as plt

def collatz_sequence_length_non_optimized(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def longest_collatz_sequence_non_optimized(x):
    max_length = 0
    number_with_max_length = 1
    
    for i in range(1, x + 1):
        current_length = collatz_sequence_length_non_optimized(i)
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i
            
    return number_with_max_length

def collatz_sequence_length_optimized(n, memo):
    original_n = n
    length = 1

    while n != 1:
        if n in memo:
            length += memo[n] - 1
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1

    memo[original_n] = length
    return length

def longest_collatz_sequence_optimized(x):
    memo = {}
    max_length = 0
    number_with_max_length = 1
    
    for i in range(1, x + 1):
        current_length = collatz_sequence_length_optimized(i, memo)
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i
            
    return number_with_max_length

def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result

if __name__ == "__main__":
    inputs = [1000, 10000, 100000, 1000000, 5000000, 10000000]
    non_optimized_times = []
    optimized_times = []

    for x in inputs:
        non_opt_time, _ = time_function(longest_collatz_sequence_non_optimized, x)
        opt_time, _ = time_function(longest_collatz_sequence_optimized, x)
        non_optimized_times.append(non_opt_time)
        optimized_times.append(opt_time)
        print(f"For input {x}: Non-optimized time = {non_opt_time:.4f} seconds, Optimized time = {opt_time:.4f} seconds")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(inputs, non_optimized_times, label='Non-Optimized', marker='o')
    plt.plot(inputs, optimized_times, label='Optimized', marker='o')
    plt.xlabel('Input Value')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison of Collatz Sequence Computation')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

