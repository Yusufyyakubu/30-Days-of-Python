# # Day 11 of 30 days of python

# # Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers(x, y):
#     total = x + y
#     return total
# print("Sum of 4 and 8 is: ", add_two_numbers(4, 8))

# # Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(radius):
#     pi = 3.14
#     area = pi * radius * radius
#     return area
# print("The area of a circle is", area_of_circle(3))

# # Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# numbers_to_add = int(input("How many numbers do you want to add? "))
# list_item = []
# while numbers_to_add > 0:
#     try:
#         num = float(input("Input number: "))
#         numbers_to_add -= 1
#         list_item.append(num)
#     except ValueError:
#         print("Only numbers are accepted")
#         break

# # print(list_item)

# items_str = ', '.join(str(item) for item in list_item)
# def add_all_nums(*nums):
#     total = 0
#     for n in nums:
#         total += n
#     return total
# print(f"The sum of {items_str} is: ", add_all_nums(*list_item))
    
# # Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# print("This programme converts from Celsius to Fahrenheit")
# celsius = float(input("Enter the Celsius temperature you want to convert as a number: "))

# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/15) + 32
#     return fahrenheit

# print(f"The value of {celsius} C is", convert_celsius_to_fahrenheit(celsius), "F")


# # Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# # Function declaration
# def check_season(month):
#     # Convert the month to lowercase for case-insensitive comparison
#     month_lower = month.lower()

#     # Define the months associated with each season
#     spring_months = ['march', 'april', 'may']
#     summer_months = ['june', 'july', 'august']
#     autumn_months = ['september', 'october', 'november']
#     winter_months = ['december', 'january', 'february']

#     # Check which season the month falls into
#     if month_lower in spring_months:
#         return 'Spring'
#     elif month_lower in summer_months:
#         return 'Summer'
#     elif month_lower in autumn_months:
#         return 'Autumn'
#     elif month_lower in winter_months:
#         return 'Winter'
#     else:
#         return 'Check your input again'

# # Functional call
# month_input = input("Enter a month: ")
# result = check_season(month_input)

# print(f"The season for {month_input.capitalize()} is {result}.")

# # Write a function called calculate_slope which return the slope of a linear equation
# # Function declaration
# def calculate_slope(coeff_x, coeff_y):
#     # Check if the coefficient of x is zero to avoid division by zero
#     if coeff_x == 0:
#         raise ValueError("The coefficient of x cannot be zero for a linear equation.")

#     # Calculate the slope (m)
#     slope = -coeff_y / coeff_x
#     return slope

# # Function call
# coeff_x = float(input("Enter the coefficient of x: "))
# coeff_y = float(input("Enter the coefficient of y: "))

# slope = calculate_slope(coeff_x, coeff_y)
# print(f"The slope of the linear equation is: {slope}")

# # Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# # Accept the values of a,b,c
# import cmath
# print("** This programme solves for a quadratic equation. **")
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))

# # Function declaration
# def solve_quadratic_eqn(a, b, c):
#     # solve for x
#     x = cmath.sqrt(b**2 - 4*a*c)

#     # solve for the roots
#     root1 = (-b + x) / (2 * a)
#     root2 = (-b - x) / (2 * a)
#     return root1, root2

# # Function call
# solution = solve_quadratic_eqn(a, b, c)
# print(f"The solution to the quadractic equation is {solution}")

# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
# def print_list_from_user_input():
#     # Get the number of items from the user
#     num_items = int(input("How many items do you want to add to the list? "))

#     # Initialize an empty list to store items
#     my_list = []

#     # Get items from the user and add them to the list
#     for _ in range(num_items):
#         item = input("Enter an item: ")
#         my_list.append(item)

#     # Print each item in the list
#     for element in my_list:
#         print(element)

# # Call the function to test it
# print_list_from_user_input()

# # Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
# num_of_items = int(input("How many items do you want to reverse?"))
# my_list = []
# for i in range(num_of_items):
#     item = input("Enter Item:")
#     my_list.append(item)
# # print(my_list)  
# def reverse_list(my_list):
#     reverse_list = []

#     for element in range(len(my_list) -1, -1, -1):
#         reverse_list.append(my_list[element])
#     return reverse_list

# print("Original List", my_list)
# print("Reversed List" , reverse_list(my_list))

# # Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(input_list):
#     # Use list comprehension to create a new list with capitalized items
#     capitalized_list = [item.capitalize() for item in input_list]
#     return capitalized_list

# # Example usage:
# my_list = ['apple', 'banana', 'orange', 'grape']
# capitalized_result = capitalize_list_items(my_list)

# print("Original list:", my_list)
# print("Capitalized list:", capitalized_result)

# # Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# def add_item(input_list, new_item):
#     # Create a new list by copying the original list and appending the new item
#     new_list = input_list.copy()
#     new_list.append(new_item)
#     return new_list

# # Example usage:
# original_list = [1, 2, 3, 4]
# new_item_to_add = 5

# result_list = add_item(original_list, new_item_to_add)

# print("Original list:", original_list)
# print("List after adding item:", result_list)

# # Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# def add_item(input_list, new_item):
#     # Create a new list with the item added at the end
#     new_list = input_list + [new_item]
#     return new_list

# # Example usage:
# original_list = [1, 2, 3, 4]
# item_to_add = input("Enter item to add: ")

# result_list = add_item(original_list, item_to_add)

# print("Original list:", original_list)
# print("List after adding item:", result_list)

# # Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def remove_item(input_list, item_to_remove):
#     # Create a new list with the item removed
#     new_list = [item for item in input_list if item != item_to_remove]
#     return new_list

# # Example usage:
# original_list = [1, 2, 3, 4, 2, 5]
# item_to_remove = 2

# result_list = remove_item(original_list, item_to_remove)

# print("Original list:", original_list)
# print("List after removing item:", result_list)

# # Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# def sum_of_numbers(n):
#     # Use the sum() function to add all numbers in the range from 1 to n
#     result = sum(range(1, n + 1))
#     return result

# # Example usage:
# number_to_sum = 5
# total_sum = sum_of_numbers(number_to_sum)

# print(f"The sum of numbers from 1 to {number_to_sum} is: {total_sum}")

# # Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(n):
#     # Use the sum() function to add all odd numbers in the range from 1 to n
#     result = sum(i for i in range(1, n + 1) if i % 2 != 0)
#     return result

# # Example usage:
# number_to_sum = 10
# total_sum_of_odds = sum_of_odds(number_to_sum)

# print(f"The sum of odd numbers from 1 to {number_to_sum} is: {total_sum_of_odds}")

# # Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(n):
#     # Use the sum() function to add all even numbers in the range from 1 to n
#     result = sum(i for i in range(1, n + 1) if i % 2 == 0)
#     return result

# # Example usage:
# number_to_sum = 10
# total_sum_of_even = sum_of_even(number_to_sum)

# print(f"The sum of even numbers from 1 to {number_to_sum} is: {total_sum_of_even}")

# # Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# def evens_and_odds(number):
#     # Initialize counters for even and odd digits
#     even_count = 0
#     odd_count = 0

#     # Iterate over each digit in the number
#     for digit in range(number + 1):
#         if digit % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#     return even_count, odd_count

# # Example usage:
# input_number = 100
# even_count, odd_count = evens_and_odds(input_number)

# print(f"Number of even digits in {input_number}: {even_count}")
# print(f"Number of odd digits in {input_number}: {odd_count}")

# # Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# def factorial(number):
#     # Check if the number is non-negative
#     if number < 0:
#         return "Factorial is undefined for negative numbers."

#     # Initialize the result to 1
#     result = 1

#     # Calculate the factorial
#     for i in range(1, number + 1):
#         result *= i

#     return result

# # Example usage:
# input_number = 5
# factorial_result = factorial(input_number)

# print(f"The factorial of {input_number} is: {factorial_result}")

# # Call your function is_empty, it takes a parameter and it checks if it is empty or not
# def is_empty(data):
#     # Check if the data is empty based on its type
#     if data is None:
#         return True
#     elif isinstance(data, (str, list, tuple, dict, set)):
#         return not bool(data)
#     else:
#         return False

# # Example usage:
# empty_string = ""
# non_empty_list = [1, 2, 3]

# print(f"Is the string empty? {is_empty(empty_string)}")  # Output: True
# print(f"Is the list empty? {is_empty(non_empty_list)}")  # Output: False

# # Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# # Mean
# def calculate_mean(data):
#     if not data:
#         return None
#     return sum(data) / len(data)

# # Median
# def calculate_median(data):
#     sorted_data = sorted(data)
#     n = len(sorted_data)
#     if n % 2 == 0:
#         mid1 = sorted_data[n // 2 - 1]
#         mid2 = sorted_data[n // 2]
#         return (mid1 + mid2) / 2
#     else:
#         return sorted_data[n // 2]

# # Mode
# from collections import Counter

# def calculate_mode(data):
#     if not data:
#         return None
#     counts = Counter(data)
#     max_count = max(counts.values())
#     mode = [key for key, value in counts.items() if value == max_count]
#     return mode

# # Range
# def calculate_range(data):
#     if not data:
#         return None
#     return max(data) - min(data)

# # Variance
# def calculate_variance(data):
#     if not data or len(data) == 1:
#         return None
#     mean = calculate_mean(data)
#     squared_diff = [(x - mean) ** 2 for x in data]
#     variance = sum(squared_diff) / (len(data) - 1)
#     return variance

# # Standard deviation
# import math

# def calculate_std(data):
#     variance = calculate_variance(data)
#     if variance is None:
#         return None
#     return math.sqrt(variance)

# data = [2, 4, 4, 4, 5, 5, 7, 9]
# print("Mean:", calculate_mean(data))
# print("Median:", calculate_median(data))
# print("Mode:", calculate_mode(data))
# print("Range:", calculate_range(data))
# print("Variance:", calculate_variance(data))
# print("Standard Deviation:", calculate_std(data))

# # Write a function called is_prime, which checks if a number is prime.
# number = int(input("Enter the number you want to check if it is a prime number: "))

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# print(f"Is {number} prime?", is_prime(number))

# # Write a functions which checks if all items are unique in the list.
# def are_all_unique(input_list):
#     # Use a set to check for uniqueness
#     seen = set()
#     for item in input_list:
#         if item in seen:
#             return False
#         seen.add(item)
#     return True

# result1 = are_all_unique([1, 2, 3, 4, 5])
# print("Are all items unique in the first list?", result1)  # Output: True

# result2 = are_all_unique([1, 2, 3, 4, 1])
# print("Are all items unique in the second list?", result2)  # Output: False

# # Write a function which checks if all the items of the list are of the same data type.
# def are_all_same_type(input_list):
#     if not input_list:
#         # An empty list is considered to have items of the same type (None type).
#         return True
    
#     first_type = type(input_list[0])
#     return all(type(item) == first_type for item in input_list)
# result1 = are_all_same_type([1, 2, 3, 4, 5])
# print("Are all items of the same data type in the first list?", result1)  # Output: True

# result2 = are_all_same_type([1, 2, 'three', 4, 5])
# print("Are all items of the same data type in the second list?", result2)  # Output: False

# # Write a function which check if provided variable is a valid python variable
# import re

# def is_valid_variable(variable_name):
#     # Check if the variable name is a valid Python identifier
#     return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable_name) is not None
# result1 = is_valid_variable("valid_variable")
# print("Is 'valid_variable' a valid Python variable?", result1)  # Output: True

# result2 = is_valid_variable("1invalid_variable")
# print("Is '1invalid_variable' a valid Python variable?", result2)  # Output: False

# Go to the data folder and access the countries-data.py file. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(data, num_languages=10):
    # Assuming 'data' is a dictionary with languages as keys and speakers as values
    sorted_languages = sorted(data.items(), key=lambda x: x[1], reverse=True)
    
    # Take the top 'num_languages' languages
    top_languages = sorted_languages[:num_languages]

    return top_languages

# Example usage:
sample_data = {
    'English': 1500,
    'Mandarin': 1100,
    'Hindi': 600,
    'Spanish': 560,
    'French': 310,
    'Arabic': 310,
    'Bengali': 230,
    'Portuguese': 220,
    'Russian': 155,
    'Urdu': 150,
    'German': 130,
    'Japanese': 125,
    'Swahili': 75,
    'Korean': 75,
    'Turkish': 75,
    'Italian': 65,
    'Dutch': 60,
    'Thai': 60,
    'Vietnamese': 55
}

result = most_spoken_languages(sample_data, num_languages=10)
print("Top 10 most spoken languages:", result)