def sum_even_numbers(limit: int) -> int:
    total = 0
    for num in range(1, limit + 1):
        print(f"Current number: {num}")
        if num % 2 == 0:
            print(f"Even number found: {num}")
            total += num
        else:
            print(f"Odd number skipped: {num}")
    return total


if __name__ == "__main__":
    result = sum_even_numbers(10)
    print(f"Sum of even numbers = {result}")
