"""Login with a limited number of attempts (accumulator pattern)."""


def login():
    password = 1234
    attempts = 0  # accumulator
    max_attempts = 3

    print("you have three attempts to log in")
    while attempts < max_attempts:
        try:
            enter = int(input("enter a four-digit password: "))

            if enter == password:
                print("access granted!")
                break
            attempts += 1
            remain = max_attempts - attempts
            if remain > 0:
                print("access denied, you have", remain, "attempts left")

        except ValueError:
            print("invalid input. Please enter a number.")

    if attempts == max_attempts:
        print("access denied.")


if __name__ == "__main__":
    login()
