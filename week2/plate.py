def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    if s[0].isalpha() and s[1].isalpha():
        if len(s) >= 2 and len(s) <= 6:
            if s.isalnum():
                if s.isalnum() and s[-1].isdigit():
                    for i in range(len(s)):
                        if s[i].isdigit():
                            if s[i] == "0":
                                return False
                            else:
                                return True
                else:
                    return False
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