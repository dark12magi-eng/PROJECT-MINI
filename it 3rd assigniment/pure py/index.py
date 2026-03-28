def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


while True:
    print("\n===== PYTHON MINI SYSTEM =====")
    print("1. Add Two Numbers")
    print("2. Odd or Even")
    print("3. Loop 1 to 10")
    print("4. Largest of Three Numbers")
    print("5. Factorial")
    print("6. Multiplication Table")
    print("7. If vs Else If")
    print("8. Loop Example")
    print("9. Salary Automation System")
    print("10. Banking + School System")
    print("0. Exit")

    choice = input("Choose option: ")

    # 1 Add
    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    # 2 Odd Even
    elif choice == "2":
        n = int(input("Enter number: "))
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")

    # 3 Loop
    elif choice == "3":
        for i in range(1, 11):
            print(i, end=" ")
        print()

    # 4 Largest
    elif choice == "4":
        x = int(input("Enter number 1: "))
        y = int(input("Enter number 2: "))
        z = int(input("Enter number 3: "))
        print("Largest =", max(x, y, z))

    # 5 Factorial
    elif choice == "5":
        n = int(input("Enter number: "))
        print("Factorial =", factorial(n))

    # 6 Multiplication Table
    elif choice == "6":
        n = int(input("Enter number: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    # 7 If vs Else If
    elif choice == "7":
        num = int(input("Enter number: "))
        if num > 10:
            print("Greater than 10")
        elif num == 10:
            print("Equal to 10")
        else:
            print("Less than 10")

    # 8 Loop Example
    elif choice == "8":
        n = int(input("Enter loop number: "))
        for i in range(1, n+1):
            print(i, end=" ")
        print()

    # 9 Salary System
    elif choice == "9":
        salary = int(input("Enter salary: "))
        bonus = int(input("Enter bonus: "))
        tax = salary * 0.1
        total = salary + bonus - tax

        print("Salary:", salary)
        print("Bonus:", bonus)
        print("Tax (10%):", tax)
        print("Final Salary:", total)

    # 10 Banking + School
    elif choice == "10":
        balance = 1000
        deposit = int(input("Enter deposit amount: "))
        balance += deposit
        print("Bank Balance:", balance)

        marks = int(input("Enter student marks: "))
        if marks >= 50:
            print("Student Result: Pass")
        else:
            print("Student Result: Fail")

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")