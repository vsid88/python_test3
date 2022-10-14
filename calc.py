circle = 1
selection = 0
while circle == 1:
    print("Select Math Operation")
    print("1-Add")
    print("2-Subtract")
    print("3-Multiply")
    print("4-Divide")
    selection = input("choose your option: ")
    try:
        if selection == '1':
            addition_number_1 = int(input("1st Number: "))
            addition_number_2 = int(input("2nd Number: "))
            print(addition_number_1, "+", addition_number_2, "=", addition_number_1 + addition_number_2)
        elif selection == '2':
            subtract_number_1 = int(input("1st Number: "))
            subtract_number_2 = int(input("2nd Number: :"))
            print(subtract_number_1, "-", subtract_number_2, "=", subtract_number_1 - subtract_number_2)
        elif selection == '3':
            multiply_number_1 = int(input("1st Number: "))
            multiply_number_2 = int(input("2nd number: "))
            print(multiply_number_1, "x", multiply_number_2, "=", multiply_number_1 * multiply_number_2)
        elif selection == '4':
            division_number_1 = int(input("1st Number: "))
            division_number_2 = int(input("2nd Number: "))
            print(division_number_1, "/", division_number_2, "=", division_number_1 / division_number_2)
        elif selection == 'Exit':
            circle = 0
        else:
            print("%d Make a valid selection." % selection)
    except Exception:
        print('ivalid operation')
    except ValueError and TypeError:
        print("%r Make a valid selection" % selection)
