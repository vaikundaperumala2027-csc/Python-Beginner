def digit_step(number):
    digits = str(number)
    descending = int("".join(sorted(digits, reverse=True)))
    ascending = int("".join(sorted(digits)))
    return descending - ascending
def play_digit_game(number):
    if not 10 <= number <= 99:
        print("Please enter a two-digit number.")
        return
    if len(set(str(number))) == 1:
        print("Choose a number with two different digits.")
        return
    moves = 0
    print("Starting number:", number)
    while number != 9:
        number = digit_step(number)
        moves += 1
        print(f"Move {moves}: {number:02d}")
    print("Congratulations! You reached 9.")
    print("Total moves:", moves)
number = int(input("Enter a two-digit number: "))
play_digit_game(number)
76