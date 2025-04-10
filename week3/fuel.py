def main():

     while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if x == y:
                print("F")
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            if y == 0 or x>y:
                continue
            percentage = (x / y) * 100
            if percentage < 1:
                print("E")
                break
            elif percentage > 99:
                print("F")
                break
            else:
                print(f"{(x / y):.0%}")
                break

main()