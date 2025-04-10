def main():
    grocery = {}
    while True:
        try:
            item = input("Item: ").title()
            if item == "":
                break
            elif item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            break
        else:
            print(grocery)
    print(grocery)
main()