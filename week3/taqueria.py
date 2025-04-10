def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            if item == "":
                break
            elif item not in menu:
                raise KeyError
            else:
                total += menu[item]
        except KeyError:
            print("Item not found")
        except EOFError:
            break
        except ValueError:
            print("Invalid input")
        else:
            print(f"Total: ${total:.2f}")
    print(f"Total: ${total:.2f}")




main()