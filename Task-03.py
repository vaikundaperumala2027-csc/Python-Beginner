while True:
    print("\n--- Distance Converter ---")
    print("1. Kilometres to Miles")
    print("2. Metres to Kilometres")
    print("3. Miles to Kilometres")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        km = float(input("Enter distance in kilometres: "))
        miles = km * 0.621371
        print("Distance in miles =", round(miles, 3))
    elif choice == 2:
        metres = float(input("Enter distance in metres: "))
        km = metres / 1000
        print("Distance in kilometres =", round(km, 3))
    elif choice == 3:
        miles = float(input("Enter distance in miles: "))
        km = miles * 1.60934
        print("Distance in kilometres =", round(km, 3))
    elif choice == 4:
        print("Thank you for using Distance Converter!")
        break
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")