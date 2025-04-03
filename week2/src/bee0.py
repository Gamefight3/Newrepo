WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary

    print("That's the game!")


main()
