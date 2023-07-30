print("Hello Python!") # Prints Hello Python
print('Hello Python!') # Prints Hello Python
first_name = "John"
last_name = "Abraham"
print(f"{first_name} {last_name}")

a = 20
b = 2
print(a / b) # '/' is the operator for division

a = 20
b = '2'
print(a / int(b)) # int() converts str to int 

# Calculate car cost 
car_price = 20000
tax = 7.25
total_price = car_price * (1 + tax/100)
print(f"{total_price}")

# Concatenating and displaying strings
first_part = "Stay hungry."
second_part = "Stay foolish."
print(first_part + ' ' + second_part)

a = 'True'
b = 'FALSE'
print(a != b) # Should print "True"

a = True
b = False
print(a != b) # Should print True

# Piggy Bank 
balance = 10
withdraw = 11

if balance > withdraw:
    balance -= withdraw
    print("${balance} left in the piggy bank.")
else:
    print("Uh-oh! Not enough cash in the piggy bank.")

#odd or even
number = 3
result = "unknown"

if number % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"{number} is {result}")

# Print the distance between the Sun and Planets
planet = "Mars"
distance_from_sun = "unknown"

if planet == "Mercury":
    distance_from_sun = 57.91
elif planet == "Venus":
    distance_from_sun = 108.2
elif planet == "Earth":
    distance_from_sun = 149.6
elif planet == "Mars":
    distance_from_sun = 227.9

print(f"{planet} is {distance_from_sun} million km away from the Sun")

# Hypothetical Zoo
day = "weekday"
time = "morning"
animals = "unknown"
zoo_closed = False

if day == "weekday":
    # Check time
    if time == "morning":
        animals = "lions"
    elif time == "afternoon":
        animals = "elephants"
    else:
        zoo_closed = True
elif day == "weekend":
    # Check time
    if time == "morning":
        animals = "pandas"
    elif time == "afternoon":
        animals = "penguins"
    else:
        zoo_closed = True

if zoo_closed:
    print("The Zoo is closed.")
else:
    print(f"You can see the {animals}.")

# Celsius to Fahrenheit converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))  # Should print 32.0

# Travel Time Calculator
def travel_time(distance, speed):
    time = distance / speed
    return time

distance = 600  # distance in miles
speed = 60  # speed in mph

print(f"Travel time: {travel_time(distance, speed)} hours")

# Calculate area
def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(10, 5)
print(f"The area of the rectangle is {area} square units.")

# Countdown through while loop
def countdown(n):
    while n > 0:
        print(n)
        n -= 1

countdown(5)

# Print Odd numbers
def print_odd_numbers():
    i = 1
    while i < 100:
        print(i)
        i += 2

print_odd_numbers()

# Print numbers through for loop
def print_numbers():
    # i = 0
    for i in range(5):
        print(i)

print_numbers()

for i in range(1, 11):
    if i == 5:
        continue
    elif i > 7:
        break
    print(i)

# List of numbers
numbers = [1,2,3,4,5]

# Print the first and last elements
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

guests = ['Alice', 'Bob', 'Joe', 'Tom']
guests[2] = 'Jenny'
print(guests)

friends = ['Alice', 'Bob', 'Charlie', 'Danny']
friends.insert(2,'Fiona')
friends.append('Ella')
print(friends)

friends = ['Alice', 'Bob', 'Charlie', 'Danny']
friends.remove('Charlie')
friends.remove('Danny')
print(friends)

desserts = ('Cheesecake', 'Apple Pie', 'Chocolate Cake')
# The manager tries to add "Carrot Cake" to the menu
desserts=list(desserts)
desserts.append('Carrot Cake')
desserts=tuple(desserts)
print(desserts)

phone_book = {"John": "555-123", "Mary": "555-456", "Jane": "555-789"}
print(phone_book['John'])

shopping_list = {"apples": 10, "bananas": 5, "oranges": 10, "kiwis": 3}
# print(shopping_list["oranges"])
shopping_list['oranges'] = 15
print(shopping_list["oranges"])

inventory = {"Hydrochloric Acid": 10, "Sodium Hydroxide": 5, "Hydrogen Peroxide": 3, "Ethanol": 15}
# print(inventory)
del inventory['Hydrogen Peroxide']
print(inventory)

def safe_division(numerator, divisor):
    # handle ZeroDivisionError exception and return "Cannot divide by zero."
    try:
        return numerator / divisor
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        
print(safe_division(5, 0))

from datetime import date

def unusual_birthday(birth_year:int)-> int:
    # raise ValueError is birth_year < 1900 or birth_year > current year
    current_year = date.today().year
    if (birth_year<1900) | (birth_year > current_year):
        raise ValueError("Invalid birth year.")
    else:
        # Calculate the age
        age = current_year - birth_year
    return age


