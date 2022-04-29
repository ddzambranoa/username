import random
from datetime import date


def generator_username():
    while True:
        try:
            today_date = date.today()
            name_length = input("Please enter your first name: ").lower()
            name = name_length.split(" ")
            last_name_length = input("Please enter your last name: ").lower()
            last_name = last_name_length.split(" ")
            if name[0].isalpha() and last_name[0].isalpha():
                if len(name) >= 1 and len(last_name) >= 1:
                    username = (name[-1][:random.randrange(1, (len(name_length)-1))] + last_name[-1][:random.randrange(1, (len(last_name_length)-1))] + '{:03d}'.format(random.randrange(0, today_date.year)))
                    print(username)
                    break
                else:
                    print("Please input your full and last name.")
            else:
                print("FULL NAME can contain only letters")
        except ValueError:
            print("Something went wrong")


if __name__ == "__main__":
    generator_username()
