def collatz_sequence_length(n):
    length = 1
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        length += 1
    print(f"{sequence[0]}: {sequence}")
    return length

def longest_collatz_sequence(x):
    max_length = 0
    number_with_max_length = 1
    
    for i in range(1, x + 1):
        current_length = collatz_sequence_length(i)
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i
            
    return number_with_max_length

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    result = longest_collatz_sequence(x)
    print(f"The number between 1 and {x} with the longest Collatz sequence is: {result}")

