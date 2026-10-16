print("Welcome to the 3-Digit Number Mystery!")
number = int(input("Enter a 3-digit number: "))
moves = 0
if not 100 <= number <= 999:
    print("Invalid number. Enter a 3-digit number.")
elif len(set(str(number))) == 1:
    print("Choose a number with at least two different digits.")
else:
    print("Starting number:", number)
    while number != 495:
        digits = f"{number:03d}"
        # Separate characters
        a = digits[0]
        b = digits[1]
        c = digits[2]
        print("\nCharacters:")
        print("a =", a)
        print("b =", b)
        print("c =", c)
        # Arrange digits
        ascending = int("".join(sorted([a, b, c])))
        descending = int("".join(sorted([a, b, c], reverse=True)))
        print("Ascending:", f"{ascending:03d}")
        print("Descending:", f"{descending:03d}")
        # Calculate result
        number = descending - ascending
        moves += 1
        print("Move", moves, ":", f"{number:03d}")
    print("\nMission completed!")
    print("Kaprekar's constant:", number)
    print("Total moves:", moves)