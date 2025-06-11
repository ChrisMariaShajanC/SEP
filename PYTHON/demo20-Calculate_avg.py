def calculate_average(numbers):
    try:
        if not numbers:
            raise ValueError("List is empty.")

        total = 0
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise TypeError("List contains non-numeric values.")
            total += num

        average = total / len(numbers)
        return average

    except ValueError as ve:
        print("ValueError:", ve)

    except TypeError as te:
        print("TypeError:", te)

    finally:
        print("Computation Done")


user_input = input("Enter numbers separated by spaces: ")

try:
    numbers_list = [float(x) for x in user_input.split()]
except ValueError:
    print("Invalid input: Please enter only numbers separated by spaces.")
    numbers_list = []

result = calculate_average(numbers_list)
if result is not None:
    print("Average:", result)
