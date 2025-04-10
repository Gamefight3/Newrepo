

def main():
    price = 50
    while price > 0:
        print(f"Ammount due: {price}")
        s = int(input("Insert coin: "))
        if s in [5, 10, 25]:
            price = (price - s)
        else:
            price = price
    print(f"Change owed: {abs(price)}")
        



main()