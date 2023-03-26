# Define custom exception classes with custom messages
class NegativeNumberException(Exception):
    def __init__(self, message="The number must be non-negative"):
        self.message = message
        super().__init__(self.message)

class ZeroNumberException(Exception):
    def __init__(self, message="The number cannot be zero"):
        self.message = message
        super().__init__(self.message)

class EvenNumberException(Exception):
    def __init__(self, message="The number must be odd"):
        self.message = message
        super().__init__(self.message)

# Function that raises different custom exceptions based on input number
def my_function(num):
    if num < 0:
        raise NegativeNumberException()
    elif num == 0:
        raise ZeroNumberException()
    elif num % 2 == 0:
        raise EvenNumberException()
    else:
        print(f"The square of {num} is {num**2}")

# Call the function with different inputs
try:
    my_function(-5)
except NegativeNumberException as e:
    print(e)

try:
    my_function(0)
except ZeroNumberException as e:
    print(e)

try:
    my_function(4)
except EvenNumberException as e:
    print(e)

my_function(3)
