import math
from pandas import DataFrame
from time import sleep

round_val = 5


# options module
def options():
    print("So, What are we doing today?")
    print("Choose an option from the list below: ")
    print("[+] Simple")
    print("    1. Add")
    print("    2. Subtract")
    print("    3. Multiply")
    print("    4. Divide")
    print(" ")
    print("[+]Percentage")
    print("    5. Percent of(a% of b)")
    print("    6. Percent in(% of a in b)")
    print(" ")
    print("[+]Advanced")
    print("    7. Power of(a^b)")
    print("    8. Square Root(√a)")
    print(" ")
    print("[+]Trigno")
    print("    9. sin(a), a in degrees")
    print("   10. cos(a), a in degrees")
    print("   11. tan(a), a in degrees")
    print(" ")
    print("[+]Shapes: Gives Perimeter, Area and Diagonal/Diameter")
    print("   12. Square")
    print("   13. Rectangle")
    print("   14. Circle")
    print(" ")
    print(" ")
    print("[+]Info and More")
    print("   15. About this Program")
    print("   16. About Creator")


# addition module
def add():
    print("[+] Addition")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    solution = 0
    math_on = True
    while math_on:
        inp = float(input("[+] "))
        if inp == "":
            math_on = False
        else:
            values.append(inp)
            solution += inp
    return values, solution


# subtraction module
def subtract():
    print("[-] Subtraction")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    first_sol = float(input("[-] "))
    values.append(str(first_sol))
    solution = first_sol
    math_on =True
    while math_on:
        inp = input("[-] ")
        if inp == "":
            math_on = False
        else:
            values.append(str(inp))
            solution -= float(inp)
    return values, solution


# multiplication module
def multiply():
    print("[*] Multiplication")
    print("Enter the values one by one, when done, leave the last space blank and press Return/Enter")
    print(" ")
    values = []
    first_sol = float(input("[*] "))
    values.append(str(first_sol))
    solution = first_sol
    math_on = True
    while math_on:
        inp = input("[*] ")
        if inp == "":
            math_on = False
        else:
            values.append(inp)
            solution *= float(inp)
    return values, solution


# divison module
def division():
    print("[/] Division")
    print("Example: a/b, where a is Dividend and b is Divisor")
    print(" ")
    val1 = float(input("[/] Enter the Dividend(a): "))
    val2 = float(input("[/] Enter the Divisor(b): "))
    print("[/] Division")
    print(" ")
    return [str(val1), str(val2)], round(val1 // val2, round_val)


# percent of module - a% of b
def percentof():
    print("[%] Percent of(a% of b)")
    print("Example: a% of b")
    print(" ")
    a = float(input("[%] Enter first value(a): "))
    b = float(input("[%] Enter second value(b): "))
    return [str(a), str(b)], round(((a / 100) * b), round_val)


# percent in module - % of a in b
def percentin():
    print("[%] Percent in (% of a in b)")
    print("Example: % of a in b")
    print(" ")
    a = float(input("[%] Enter the first value(a): "))
    b = float(input("[%] Enter the second value(b): "))
    return [a, b], round(((a / b) * 100), round_val)


# power of where a^b
def power():
    print("[^] Power of(a^b)")
    print("Example: a^b or a to the power of b")
    print(" ")
    a = float(input("[^] Enter the Base(a): "))
    b = float(input("[^] Enter the Power(b): "))
    return [a, b], a ** b


# square root
def sqrt():
    print("[√] Square Root(√a)")
    print("Example: √a")
    print(" ")
    a = float(input("[√] Enter the value(a): "))
    return [a], round(a ** 0.5, round_val)


# sin
def sin():
    print("[O] sin(a), a in degrees")
    print("Example: sin(a) where a is in degrees")
    print(" ")
    a = float(input("[O] Enter the value(a): "))
    return [a], round(math.sin(math.radians(a)), round_val)


# cos
def cos():
    print("[O] cos(a), a in degrees")
    print("Example: cos(a) where a is in degrees")
    print(" ")
    a = float(input("[O] Enter the value(a): "))
    return [a], round(math.cos(math.radians(a)), round_val)


# tan
def tan():
    print("[O] tan(a), a in degrees")
    print("Example: tan(a) where a is in degrees")
    print(" ")
    a = float(input("[O] Enter the value(a): "))
    return [a], round(math.tan(math.radians(a)), round_val)


# square- perimeter, area, diagonal
def square():
    print("[-] Square")
    a = float(input("[=] Enter the length of side of the square(a): "))
    return [a], 4 * a, a ** 2, round((2 ** 0.5) * a, round_val)


# rectangle- perimeter, area, diagonal
def rectangle():
    print("[-] Rectangle")
    a = float(input("[=] Enter the length of rectangle(l): "))
    b = float(input("[=] Enter the width of rectangle(w): "))
    return [a, b], 2 * (a + b), a * b, round((((a ** 2) + (b ** 2)) ** 0.5), round_val)


# circle- circumference, area, diameter
def circle():
    print("[-] Circle")
    a = float(input("[=] Enter the radius of the circle(r): "))
    return [a], round(2 * math.pi * a, round_val), round(math.pi * a * a, round_val), 2 * a


# copy result
def ask_save(rslt):
    resp2 = input("Do you want to copy the results to your clipboard? ").upper()
    if resp2 in ['YES', 'Y']:
        df = DataFrame([rslt])
        df.to_clipboard(index=False, header=False)
    return "Copied the result to your clipboard!"


# restart app
def restart_app():
    resp = input("Do you want to start again? ").upper()
    if resp in ['YES', 'Y']:
        print(" ")
        return True


# main code
print("Welcome to my AdvancedCalculator!")
print(
    "This project is entirely made in Python as a learning milestone. If you have any suggestion, make sure to comment on this repo on GitHub!")
print("Anyways, lets get started!")
print(" ")


app_on = True
while True:
    while app_on:
        print("All solutions given by this program are rounded off to 5 decimals as default.")
        round_new = input("If you wish to change to your choice, enter the number, or leave it blank to use the default: ")
        if round_new == '':
            print("The default of 5 decimal places is being used!")
            print(" ")
        else:
            try:
                round_val = int(round_new)
                print(f"Results are now rounded off at {round_val} decimal places.")
                print(" ")
            except ValueError:
                print("Please enter an Integer value!")

        # prints options
        options()
        print(" ")

        opt = 0
        while opt not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            try:
                opt = int(input("Enter your choice: "))
            except ValueError:
                print("Error, You need to enter a number!")
            if opt == 1:
                a = add()
                print(f"{' + '.join(a[0])} = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 2:
                a = subtract()
                print(f"{' - '.join(a[0])} = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 3:
                a = multiply()
                print(f"{' x '.join(a[0])} = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 4:
                a = division()
                print(f"{'/'.join(a[0])} = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 5:
                a = percentof()
                print(f"{a[0][0]}% of {a[0][1]} is {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 6:
                a = percentin()
                print(f"{a[0][0]} is {a[1]}% of {a[0][1]}")
                ask_save({a[1]})
                break
            elif opt == 7:
                a = power()
                print(f"{a[0][0]}^{a[0][1]} is {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 8:
                a = sqrt()
                print(f"Square root of {a[0][0]} is {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 9:
                a = sin()
                print(f"sin({a[0][0]}) = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 10:
                a = cos()
                print(f"cos({a[0][0]}) = {a[1]}")
                ask_save({a[1]})
                break
            elif opt == 11:
                a = tan()
                print(f"tan({a[0][0]}) = {a[1]}")
                ask_save({a[1]})
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
        break

    if not restart_app():
        print(" ")
        print("-----------------------")
        print("Thanks for using this app! Hit me up on Discord: mightykiller#9119")
        print("-----------------------")
        sleep(4)
        break
