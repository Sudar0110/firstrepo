def check_even_odd(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return f"{number} is even."
        else:
            return f"{number} is odd."
    except ValueError:
        return "Invalid input. Please enter an integer."

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a number: ")
    result = check_even_odd(user_input)
    print(result)