from utils import calculate_sum
from insecure import get_password

def main():
    # Bug: dividing by zero if input is 0
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Sum:", calculate_sum(x, y))
    print("Division:", x / y)  # Possible ZeroDivisionError

    # Security issue: printing password
    password = get_password()
    print(f"Your password is {password}")  # Sensitive info leak

if __name__ == "__main__":
    main()
