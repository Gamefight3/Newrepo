
def main():
    user_input = input("Enter a string: ")
    print(convert(user_input))



def convert(user_input):
    user_input = user_input.replace(':)', '🙂')
    user_input = user_input.replace(':(', '🙁')
    return user_input

main()