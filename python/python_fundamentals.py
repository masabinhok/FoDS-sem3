# # # Undestanding variables

# # # A variable is a name given to a value stored in memory.
# # # Python uses dynamic typing, meaning you dont have to declare the type of a variable, it's inferred when you assign a value
# # # Variables are case sensitive, sabin and Sabin are different.
# # # Variables name must start with a letter or underscore(_).
# # # Reserved keyword like for if, class cannot be used as variable names.

# # name = "Sabin" #string
# # age = 19 #integer
# # is_student = True #boolean, true or false;
# # print (name, age, is_student)


# # # Data Types

# # # Primitive data types
# # # int, float, str, bool, None: none represents no value;
# # x = 69
# # marks = 96.69
# # campus = "Pulchowk"
# # is_good = True
# # nothing = None

# # # Q1: what do you mean by primitive datatypes?
# # # ans: they are the fundamental, most basic data types provided by the programming language as their built in data types, which are atomic. simply compare to mass length and time as the fundamental physical quantities and others are derived from them.

# # # Checking Data Types
# # print(type(campus))
# # print(isinstance(marks, float))


# # # Type Conversion

# # a = int(3.9) # float to int: 3
# # b = str(42) # int to str: 42
# # c = bool(0) # int to bool : False
# # print(a, b, c)

# # # Mutable vs. Immutable Types

# # # Mutable : can be changed after creation: list, dict, set;
# # # Immutable: cannot be changed after creation: int, float, tuple, str;

# # my_list = [1, 2, 3]
# # my_list[0] = 10 #changing the list after creation
# # print(my_list)

# # my_tuple = (1, 2, 3)
# # # my_tuple[0] = 10 (error)

# # # Q2: are you sure int and float and str are immutable?
# # # and: Yeah, i am sure they are immutable, you may feel like they aren't, cause you can modify them after created.

# # # but here's the catch, when you modify an immutable object python doesnot actaully change the object, instead it creates a new object and assigns it to the variable, we can confirm this my checking their memory address

# # check = 69
# # print(f'Original: {id(check)}')

# # check +=96
# # print(f'Modified: {id(check)}')


# # # Best practices

# # # Use meaningful variable names: user_age, total_price
# # # Constants are written in Uppercase
# # # Avoid using one letter names unless in loop.


# # # Exercise 1
# # my_name = "Sabin Shrestha"
# # my_age = 19
# # i_am_a_python_learner = True
# # print(type(my_name), type(my_age), type(i_am_a_python_learner))


# # print(f'{my_name}, {float(my_age)}')


# # # Extra

# # # Reserved Keywords
# # import keyword
# # print((keyword.kwlist))

# # # Proper way to modify a tuple
# # my_tuple = (10,) + my_tuple[1:]
# # print(my_tuple)

# # # NoneType example

# # def no_value(): 
# #   return None

# # print(no_value())

# # # Boolean conversion explaination
# # print(bool("")) # empty xa so false, 
# # print(bool(0)) # 0 is false
# # print(bool([])) # empty list so false
# # print(bool(1)) # 1 is true



# # # Loops and conditional statements

# # # used to execute certain codes based on conditions
# # # if elif else

# # # if condition: 
# # #   #code
# # # elif condtion: 
# # #   #code
# # # else: 
# # #   #code

# # # Basic example
# # roll = 69
# # if roll == 69: 
# #    print("Sabin Shrestha")
# # elif roll == 21:
# #     print("Krish CN")
# # else: 
# #    print("Kiska roll number he bhai?")


# # ## Loops 

# # # for loop, while loop, 
# # # for loop: iterate over a sequence like a list typle string or range
# # # while loop: repeat as long as the condition is true

# # # For loop

# # # for num in numbers:

# # fruits = ['apple', 'banana', 'orange']
# # for fruit in fruits: 
# #   print(fruit)

# # for i in range (1, 10):
# #   print(i)

# # # while loop

# # counter = 0

# # while counter < 5: 
# #   print(counter)
# #   counter+=1

# # # Loop control statements

# # # break: terminate/ exit the loop completely
# # # continue : skip the rest of the current iteration and move to the next
# # # else : executes after the loop finishes, unless terminated with break.

# # print("Breaks and continues\n\n")

# # for i in range (5):
# #   if ( i  == 2):
# #     break
# #   print(i)
# # else: 
# #   print("Finished without break")

# # for i in range (5):
# #   if( i == 2):
# #     continue
# #   print(i)
# # else:
# #   print("Finished without break")



# # # Combining loops and conditions
# # num = 30 
# # is_prime = True

# # for i in range(2, int(num ** 0.5) + 1): 
# #   if num % i == 0:
# #     is_prime = False
# #     break

# # if is_prime: 
# #   print(f'{num} is prime')
# # else:
# #   print(f'{num} is not prime')


# # # Exercise 2:

# # # wap to calcualte the sum of all numbers between 1 and 50 that are divisible by 3.

# # sum = 0
# # for i in range(1, 50):
# #   if i % 3 == 0: 
# #     sum = sum + i

# # print(sum)

  
# # # wap to create a multiplication table for a given number using a loop

# # num  = 2

# # for i in range(1, 11):
# #   print(f'{num} * {i} = {num * i}')


# # # wap that prints all the vowels in a given string

# # given_string = "Sabin Shrestha"
# # lowercased_string = given_string.lower()


# # for letter in lowercased_string:
# #   if letter in 'aeiou':
# #     print(letter)


# # ## FUNCTIONS AND SCOPE

# # def greet(name):
# #   return f"Heloo, {name}!"

# # print(greet("Sabin"))

# def greet(name='Friend'):
#   return f"Heloo, {name}!"

# print(greet("Sabin"))
# print(greet())

# def add(a, b):
#   return a + b

# print(add(3, 5))

# # keyword arguments, specify the value of arguments while calling the function
# def multiply(a, b):
#     print(f'a: {a} * b: {b} = {a*b}')

# multiply(b = 3, a = 2)

# def sum_all(*numbers):
#   return sum((numbers))


# print(sum_all(1, 2, 3, 4, 5))

# def display_info(**students):
#   print(students.items())
#   for key, value in students.items():
#     print(f"{key}: {value}")
  
# display_info(name="Sabin", age =22, country="Nepal")



# # Lambda functions:

# square = lambda x: x ** 2
# print(square(2))


# ## Scope in python

# # scope refers to the region of code where a varaiable is accessible


# s = 10 # global variable

# def print_s():
#   y = 10 # local varibale, 
#   print(s) # s is a global variable so it is accessible here inside the function, 


# print_s()
# # print(y) # error, it is not accessible here


# def print_y():
#   y = 5
#   print(y)

# print_y()  # this is okay because when we call this function, the variable is accessible again, cause we are printing it inside the function itself.



# global keyword
count = 0

def increment():
  global count  # we have to redeclare a global variable in order to modify, it is accessible for readonly typa, thing.
  count +=1

increment()
increment()
increment()
print(count)


def outer_func():
  outer_var = 10

  def inner_func():
    nonlocal outer_var
    outer_var += 5
    print(outer_var)

  inner_func()
  print(outer_var)


outer_func()

  
















