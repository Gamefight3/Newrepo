def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
                if s[-2:].isalnum() and s[:-2].isalpha():
                    for i in range(len(s)):
                        if s[i].isdigit():
                            if s[i] == "0":
                                return False
                            else:
                                return True
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
#Much like a list, a str is a “sequence” (of characters), which means it can be
#  “sliced” into shorter strings with syntax like s[i:j]. For instance, if s is "CS50",
# then s[0:2] would be "CS".

main()


#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”