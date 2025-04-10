def main():
    # Prompt the user for a date in the format MM/DD/YYYY
    # and print the month name corresponding to the month number.

    list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
            try:
                month, day, year = input("Date: ").split("/")
                try:
                        month = int(month)
                except ValueError:
                        if month in list:
                            month = int(list.index(month) + 1)
                        else:
                            pass
                day = int(day)
                year = int(year)
            except ValueError:
                pass
            else:
                  if day <0 or day > 32:
                        pass
                  elif month < 0 or month > 12:
                        pass
                  else:
                        print(f"{year}-{month:02}-{day:02}")
                        break

main()
