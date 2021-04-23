import math
# from pandas import DataFrame
from time import sleep

round_val = 5


# options module
def options():
    print("So, What are we doing today?")
    print("Choose an option from the list below: ")
    print("[+] Simple                                   [+]Trigno")
    print("    1. Add                                       9. sin(a), a in degrees")
    print("    2. Subtract                                 10. cos(a), a in degrees")
    print("    3. Multiply                                 11. tan(a), a in degrees")
    print("    4. Divide")
    print(" ")
    print("[+]Percentage                                [+]Shapes: Gives Perimeter, Area and Diagonal/Diameter")
    print("    5. Percent of(a% of b)                      12. Square")
    print("    6. Percent in(% of a in b)                  13. Rectangle")
    print("                                                14. Circle")
    print(" ")
    print("[+]Advanced                                  [+]Info and More")
    print("    7. Power of(a^b)                            15. About this Program")
    print("    8. Square Root(√a)                          16. About Creator")
    print("                                                17. Quit this Program")


# addition module
def add():
    print("[+] Addition")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    solution = 0
    math_on = True
    while math_on:
        try:
            inp = input("[*] ")
            if inp != "":
                values.append(float(inp))
            elif inp == "":
                math_on = False
        except ValueError:
            print("Please enter a number!")
    for _ in values:
        if _ == "":
            break
        else:
            solution += float(_)
            values[values.index(_)] = str(_)
    return values, solution


# subtraction module
def subtract():
    print("[-] Subtraction")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    solution = 0
    math_on = True
    while math_on:
        try:
            inp = input("[*] ")
            if inp != "":
                values.append(float(inp))
            elif inp == "":
                math_on = False
        except ValueError:
            print("Please enter a number!")

    solution += values[0]
    for _ in values[1:]:
        if _ == "":
            break
        else:
            solution -= float(_)
            values[values.index(_)] = str(_)
    return values, solution


# multiplication module
def multiply():
    print("[*] Multiplication")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    solution = 1
    math_on = True
    while math_on:
        try:
            inp = input("[*] ")
            if inp != "":
                values.append(float(inp))
            elif inp == "":
                math_on = False
        except ValueError:
            print("Please enter a number!")
    for _ in values:
        if _ == "":
            break
        else:
            solution *= _
            values[values.index(_)] = str(_)
    return values, solution


# divison module
def division():
    print("[/] Division")
    print("Example: a/b, where a is Dividend and b is Divisor")
    print(" ")
    val1 = 1
    val2 = 1
    math_on = True
    while math_on:
        try:
            val1 = float(input("[/] Enter the Dividend(a): "))
            val2 = float(input("[/] Enter the Divisor(b): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [str(val1), str(val2)], round(val1 // val2, round_val)


# percent of module - a% of b
def percentof():
    print("[%] Percent of(a% of b)")
    print("Example: a% of b")
    print(" ")
    perval1 = 1
    perval2 = 1
    math_on = True
    while math_on:
        try:
            perval1 = float(input("[%] Enter first value(a): "))
            perval2 = float(input("[%] Enter second value(b): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [str(perval1), str(perval2)], round(((perval2 / 100) * perval2), round_val)


# percent in module - % of a in b
def percentin():
    print("[%] Percent in (% of a in b)")
    print("Example: % of a in b")
    print(" ")
    perinval1 = 1
    perinval2 = 1
    math_on = True
    while math_on:
        try:
            perinval1 = float(input("[%] Enter the first value(a): "))
            perinval2 = float(input("[%] Enter the second value(b): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [perinval1, perinval2], round(((perinval1 / perinval2) * 100), round_val)


# power of where a^b
def power():
    print("[^] Power of(a^b)")
    print("Example: a^b or a to the power of b")
    print(" ")
    pwr1 = 1
    pwr2 = 1
    math_on = True
    while math_on:
        try:
            pwr1 = float(input("[^] Enter the Base(a): "))
            pwr2 = float(input("[^] Enter the Power(b): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [pwr1, pwr2], pwr1 ** pwr2


# square root
def sqrt():
    print("[√] Square Root(√a)")
    print("Example: √a")
    print(" ")
    sqrtval = 1
    math_on = True
    while math_on:
        try:
            sqrtval = float(input("[√] Enter the value(a): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [sqrtval], round(sqrtval ** 0.5, round_val)


# sin
def sin():
    print("[O] sin(a), a in degrees")
    print("Example: sin(a) where a is in degrees")
    print(" ")
    sinval = 1
    math_on = True
    while math_on:
        try:
            sinval = float(input("[O] Enter the value(a): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [sinval], round(math.sin(math.radians(sinval)), round_val)


# cos
def cos():
    print("[O] cos(a), a in degrees")
    print("Example: cos(a) where a is in degrees")
    print(" ")
    cosval = 1
    math_on = True
    while math_on:
        try:
            cosval = float(input("[O] Enter the value(a): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [cosval], round(math.cos(math.radians(cosval)), round_val)


# tan
def tan():
    print("[O] tan(a), a in degrees")
    print("Example: tan(a) where a is in degrees")
    print(" ")
    tanval = 1
    math_on = True
    while math_on:
        try:
            tanval = float(input("[O] Enter the value(a): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [tanval], round(math.tan(math.radians(tanval)), round_val)


# square- perimeter, area, diagonal
def square():
    print("[-] Square")
    squareval = 1
    math_on = True
    while math_on:
        try:
            squareval = float(input("[=] Enter the length of side of the square(a): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [squareval], 4 * squareval, squareval ** 2, round((2 ** 0.5) * squareval, round_val)


# rectangle- perimeter, area, diagonal
def rectangle():
    print("[-] Rectangle")
    ln = 1
    wd = 1
    math_on = True
    while math_on:
        try:
            ln = float(input("[=] Enter the length of rectangle(l): "))
            wd = float(input("[=] Enter the width of rectangle(w): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [ln, wd], 2 * (ln + wd), ln * wd, round((((ln ** 2) + (wd ** 2)) ** 0.5), round_val)


# circle- circumference, area, diameter
def circle():
    print("[-] Circle")
    _ = 1
    math_on = True
    while math_on:
        try:
            _ = float(input("[=] Enter the radius of the circle(r): "))
            math_on = False
        except ValueError:
            print("Please enter a number!")
    return [_], round(2 * math.pi * _, round_val), round(math.pi * _ * _, round_val), 2 * _


# copy result
# def ask_save(rslt):
#    resp2 = input("Want me to copy the results to your clipboard? Only the solution is copied. ").upper()
#    if resp2 in ['YES', 'Y']:
#        df = DataFrame([rslt])
#        df.to_clipboard(index=False, header=False)
#    return "Successfully copied the result to your clipboard!"


# restart app
def restart_app():
    resp = ""
    while resp not in ['YES', 'Y', 'YUP', 'YE', 'NO', 'N', 'NOPE', 'NAH']:
        resp = input("Do you want to start over?").upper()
        if resp in ['YES', 'Y', 'YUP', 'YE']:
            return True
        elif resp in ['NO', 'N', 'NOPE', 'NAH']:
            return False
        else:
            print("Yes. or No.")
            resp = ""

    # main code


print("Welcome to my AdvancedCalculator!")
print(" ")
print("This project is entirely made in Python as a learning milestone. If you have any suggestion, make sure to "
      "comment on this repo on GitHub!")
print("Anyways, lets get started!")
print(" ")

app_on = True
while True:
    while app_on:
        print("All solutions given by this program are rounded off to 5 decimals as default.")
        roundnm = True
        while roundnm:
            try:
                round_new = input("If you wish to change to your choice, enter the number, or leave it blank to use "
                                  "the default: ")
                if round_new != "":
                    round_val = int(round_new)
                    print(f"Results are now rounded off at [{round_val}] decimal places.")
                    print(" ")
                    roundnm = False
                elif round_new == "":
                    roundnm = False
            except ValueError:
                print("Please enter an Integer value!")

        # prints options
        options()
        print(" ")

        opt = 0
        while opt not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
            try:
                opt = int(input("Enter your choice: "))
            except ValueError:
                print("Error, You need to enter a number!")
            if opt == 1:
                a = add()
                print(f"{' + '.join(a[0])} = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 2:
                a = subtract()
                print(f"{' - '.join(a[0])} = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 3:
                a = multiply()
                print(f"{' x '.join(a[0])} = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 4:
                a = division()
                print(f"{'/'.join(a[0])} = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 5:
                a = percentof()
                print(f"{a[0][0]}% of {a[0][1]} is {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 6:
                a = percentin()
                print(f"{a[0][0]} is {a[1]}% of {a[0][1]}")
                # ask_save({a[1]})
                break
            elif opt == 7:
                a = power()
                print(f"{a[0][0]}^{a[0][1]} is {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 8:
                a = sqrt()
                print(f"Square root of {a[0][0]} is {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 9:
                a = sin()
                print(f"sin({a[0][0]}) = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 10:
                a = cos()
                print(f"cos({a[0][0]}) = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 11:
                a = tan()
                print(f"tan({a[0][0]}) = {a[1]}")
                # ask_save({a[1]})
                break
            elif opt == 12:
                a = square()
                print(f"Given side: {a[0][0]}")
                print(f"Perimeter of the Square: {a[1]}")
                print(f"Area of the Square: {a[2]}")
                print(f"Diagonal of the Square: {a[3]}")
                break
            elif opt == 13:
                a = rectangle()
                print(f"Given length: {a[0][0]}")
                print(f"Given width: {a[0][1]}")
                print(f"Perimeter of the Rectangle: {a[1]}")
                print(f"Area of the Rectangle: {a[2]}")
                print(f"Diagonal of the Rectangle: {a[3]}")
                break
            elif opt == 14:
                a = circle()
                print(f"Given radius: {a[0][0]}")
                print(f"Circumference of the Circle: {a[1]}")
                print(f"Area of the Circle: {a[2]}")
                print(f"Diameter of the Circle: {a[3]}")
                break
            elif opt == 15:
                print("\n" * 100)
                print("[+] About this program:")
                print(" ")
                print("This is a small, but feature filled calculator, made entirely in Python. More features to be "
                      "added very soon!")
                print("I thank you from my heart for giving this program a try. I hope you enjoy it.")
                print(" ")
                print("[-] About the functions in the menu: ")
                print("  [>] Add: Takes two or more numbers and returns their sum. Press return/enter after each "
                      "number. When done leave blank and press return/enter at the end.")
                print("  [>] Subtract: Same as Add, just returns the result after subtracting the entered values.")
                print("  [>] Multiply: Same as Add, just returns the result after multiplying the entered values.")
                print("  [>] Divide: Takes in two numbers and divides them.")
                print("  [>] Percent of: Returns how much of a% is in b. User gives the values of a and b.")
                print("  [>] Percent in: Returns % of a in b. User gives the values of a and b.")
                print("  [>] Power of: Takes  in two values, a and b, and puts in the equation -> a^b.")
                print("  [>] Square Root: Gives the square root of the given number.")
                print("[>] Trignometric Functions(sin, cos, tan): Takes in a in degrees and returns their "
                      "trignometric values.")
                print("  [>] Shapes(Square, Rectangle, Circle): Takes side, length and width, or radius and returns "
                      "respective values(perimeter/ circumference, area, diagonal/diameter).")
                print(" ")
                print(" ")
                input("Pres Return/Enter to go back to main menu. ")
                print(" ")
                options()
                print(" ")
                opt = 0
            elif opt == 16:
                print("\n" * 100)
                print("[+] About the creator:")
                print(" ")
                print("I enjoy writing programs to help me with daily life things, nothing much. Aspiring to be a "
                      "competitive programmer one day. Nothing much. But thank you for using my program!")
                print(" ")
                print(" ")
                input("Pres Return/Enter to go back to main menu. ")
                print(" ")
                options()
                print(" ")
                opt = 0
            elif opt == 17:
                break
        break

    if not restart_app():
        print(" ")
        print("+----------------------->>>")
        print("|Thanks for using this app! Hit me up on Discord: mightykiller#9119")
        print("+----------------------->>>")
        sleep(4)
        break
