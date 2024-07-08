passwords = {"ali": "3547534", "reza": "735867357", "neda": "4524452"}

blacklist = {"neda"}
from functools import wraps


def ban(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in blacklist:
            print("This user is blocked.")
        else:
            func(*args, **kwargs)

    return inner


@ban
def print_password(username):
    print(username, ":", passwords[username])


@ban
def change_password(username, new_password):
    passwords[username] = new_password
    print(username, ":", passwords[username])


# print_password("neda")
change_password("reza", "1234")
print(passwords)
