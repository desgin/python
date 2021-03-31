class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


class ValueErrors(ValueError):
    """Raised when the input value"""
    pass


# you need to guess this number
number = 115

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("value between 1 and 115:"))

        if i_num < 1:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()
    except ValueErrors:
        print("enter a valid number")
        print()

print("Congratulations! You guessed it correctly.")