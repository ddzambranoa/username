# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# -------------------------------------------
# Username Validation
# Programmer:   https://www.linkedin.com/in/ddzambranoa/
# Created:      April 25, 2022
# Copyright:    Free
# License:      Free
# -------------------------------------------

def validation():
    while True:
        try:
            username = input("Please Enter Your Username: ")
            if username.isalnum():
                if username.islower():
                    if 6 <= len(username) <= 20:
                        print("Username", username.upper(), "was successfully entered")
                        break
                    elif len(username) < 6:
                        print("Username must contain at least 6 characters")
                    else:
                        print("Username cannot contain more than 20 characters")
                else:
                    print("Username must be lowercase")
            else:
                print("Username can contain only letters or numbers")
        except ValueError:
            print("Something went wrong")


if __name__ == "__main__":
    validation()
