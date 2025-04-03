def main():
    time = input("Enter the time in HH:MM format: ")
    if convert(time) >= 7.0 and convert(time) < 8.0:
        print("Breakfast time")
    elif convert(time) >= 12.0 and convert(time) < 13.0:
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) < 19.0:
        print("Dinner time")
    
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time_ret = 0.00
    mins = float(minutes) / 60
    time_ret = hours + mins
    return time_ret


if __name__ == "__main__":
    main()