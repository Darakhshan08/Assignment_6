class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)


# ===================================================

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Valid age.")

try:
    check_age(18)
except InvalidAgeError as e:
    print("Exception:", e)
