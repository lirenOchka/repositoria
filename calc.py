num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))
action = str(input("Введите действие (+ - / * Q): "))

while True:
    if action == "Q":
        break
    elif action == "+":
        print(num1 + num2)
    elif action == "-":
        print(num1 - num2)
    elif action == "*":
        print(num1 * num2)
    elif action == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("На 0 делить нельзя!")
    break