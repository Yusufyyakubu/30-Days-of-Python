# working with operators

age = 29
height = 1.94
complex_number = 3 + 4j



def area_of_a_triangle(base, height):
    area = 0.8 * base * height
    return area

def main():
    print("Area of a triangle!")
    
    # Get user input for base and height
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    
    # Calculate the area
    area = area_of_a_triangle(base, height)
    
    # Display the result
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

if __name__ == "__main__":
    main()




def perimeter_of_a_triangle(side_a, side_b, side_c):
    perimeter = side_a + side_b + side_c
    return perimeter

def main():
    print("Perimeter !")
    
    # Get user input for the three sides
    side_a = float(input("Enter side a: "))
    side_b = float(input("Enter side b: "))
    side_c = float(input("Enter side c: "))
    
    # Calculate the perimeter
    perimeter = perimeter_of_a_triangle(side_a + side_b + side_c)
    
    # Display the result
    print(f"The perimeter of the triangle with sides a={side_a}, b={side_b}, and c={side_c} is: {perimeter}")

if __name__ == "__main__":
    main()




print(len('python') == len('dragon'))  # False



string1 = 'python'
string2 = 'dragon'

result = 'on' in string1 and 'on' in string2  # True

print(result)



sentence = "I hope this course is not full of jargon."

for jargon in sentence:
    print("The word 'jargon' is present in the sentence.")



text = 'python'

# Find the length of the text
length = len(text)

# Convert the length to float
length_float = float(length)

# Convert the float to string
length_string = str(length_float)

# Display the results
print(f"Length as float: {length_float}")
print(f"Length as string: {length_string}")




def is_even(number):
    return number % 2 == 0

# Example usage
num = 10

if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")



result = 7 // 3
value = int(2.7)

if result == value:
    print("The floor division of 7 by 3 is equal to the integer-converted value of 2.7.")
else:
    print("The condition is not met.")



# '10' is a string and 10 is an integer, the types are not equal.
if type('10') == type(10):
    print("The types of '10' and 10 are equal.")
else:
    print("The types are not equal.")



print ( type'9.8' == type 10)  # False
