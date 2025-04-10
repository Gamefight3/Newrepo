def main():
    # List of month names
    months = [
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
            # Prompt the user for a date
            date = input("Date: ").strip()

            if "/" in date:  # Format: MM/DD/YYYY
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:  # Format: Month Day, Year
                month_name, day_year = date.split(" ", 1)
                day, year = day_year.split(", ")
                if month_name in months:
                    month = months.index(month_name) + 1
                else:
                    raise ValueError("Invalid month name")
                day = int(day)
                year = int(year)

            # Validate day and month
            if day < 1 or day > 31:
                raise ValueError("Invalid day")
            if month < 1 or month > 12:
                raise ValueError("Invalid month")

            # Print the date in YYYY-MM-DD format
            print(f"{year}-{month:02}-{day:02}")
            break
        except (ValueError, IndexError):
            # If there's an error, prompt the user again
            print("Invalid date format. Please try again.")

main()