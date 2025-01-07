# # # ## Arrays in python: arrays is just a collection of items, all of the same data type. python doesn't have built in support for array, so we have to import it


# # # import array

# # # arr = array.array('i', [1, 2, 3, 3, 4]) # i here specifies that it's a integer array.

# # # print(arr[0])

# # # arr[1] = 10
# # # print(arr)

# # # arr.append(5) # appends to the last of the array
# # # print(arr) 
# # # arr.remove(3) # removes the first found matchingt element
# # # print(arr)



# # # # Lists in python

# # # #Lists are versatile, they can hold mixed type of datas.. most widely used data structures in pythonnn

# # # # creating a list

# # # my_list = [1, "hello", 3.15, True]

# # # # access elements
# # # print(my_list[0])

# # # #slicing: slice vaneko katnu, list bata certain kura lai katera jhiknu
# # # print(my_list[1:3]) #1:3 garyo vane, values of index 1 < 3 print hunxa


# # # #modifying list;

# # # #append, insert garna milxas

# # # #append : append vaneko last ma thapnu ho

# # # my_list.append("new item1")
# # # print(my_list)


# # # # insert: insert new values in specified index
# # # my_list.insert(2, "inserteditem")
# # # print(my_list)
 
# # # # remove: removes the said value

# # # my_list.remove(3.15)
# # # print(my_list)

# # # # pop: pop le chai last index ko value lai remove ra return garxa

# # # last_item = my_list.pop()
# # # print(my_list)
# # # print(last_item)


# # # ## iterating throuhg listts

# # # for item in my_list:
# # #   print(item)

# # # squared_numbers = [x**2 for x in [1,2,3,4]]
# # # print(squared_numbers)




# # ## pracice time


# # # array
# # import array 
# # integers = array.array('i', [5, 10, 15, 20, 25])

# # integers[1] = 50

# # integers.append(30)

# # integers.remove(15)

# # print(integers)



# # def sum_array(integers):
# #   return sum(integers)
  

# # print(sum_array(integers))


# # def check_if_exists(num, array):
# #   num_exists = False
# #   index = 0
# #   for item in array:

# #     if num == item:
# #       num_exists = True
# #       print(index)
# #     index+=1
  
# #   if(num_exists == False):
# #     print("Not found")

# # def enumerate_array(num, array):
# #   for index, item in enumerate(array):
# #     if num == item:
# #       print(f"Found at index: {index}")
# #       return
    
# #   print("Not found")

# # check_if_exists(50, integers)
# # enumerate_array(5, integers)


# # 1
# fruits = ["apple", "banana", "cherry"]
# fruits.append("date")
# fruits.insert(1, "blueberry")
# fruits.remove("banana")

# fruits.reverse()
# print(fruits)

# #2 
# numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:5])
# print(numbers[7:10])
# print(numbers[0:10:2])

# #3
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)

# #couldnot solve
# even_numbers = [ x for x in numbers if x % 2 == 0]
# print(even_numbers)

# #4 
# def check_max_min(list):
#   return ( max(list), min(list))

# print(check_max_min(numbers))

# # #5 
# # def double(list):
# #   return [x*2 for x in list]

# # print(double(numbers))



# ## Tuples
# # Tuple is a immutable: vannale change garna namilne, ordered collection of elements. 

# my_tuple = (1,2,3)

# print(my_tuple[0]) # 1

# print(my_tuple[1:3]) # (2,3)

# a, b, c = my_tuple #destructuring typa thing
# print(a, b, c) # 1 2 3

# # Tuple ops:
# #Concatenation
# tuple1 = (1,2)
# tuple2=(3,4)
# result = tuple1 + tuple2
# print(result)

# #repetition 
# print(tuple1*3)

# #membership testing
# print(3 in result) 
# print(2 in tuple2)

# ## sets : sets is an unordered collection of unique elements. set do not allow duplicate values

# my_set = {1,2,3}

# #add
# my_set.add(4)
# print(my_set)


# #remove 
# my_set.remove(2)
# print(my_set)

# # membership check
# print(3 in my_set)

# ## set ops:
# #union: combines el of both sets

# set1 = {1,2,3}
# set2 = {1, 4, 7}
# print(set1 | set2) #union : |

# # intersection
# print(set1 & set2) #intersection : &

# # difference -
# print(set1 - set2) 

# # symmetric difference vaneko a-b U b-a (^)
# print(set1 ^ set2)

# ## Practice problems  

# tuples

# integers = (1,2,3,4,5, 6,7 ,8, 9,10)
# print(integers[0:5])
# print(integers[5:10])
# print(integers[0:10:2])

# # def tuple_ops(my_tuple):
# #   prod = 1
# #   for item in my_tuple:
# #     prod*=item
# #   return (sum(my_tuple), prod )

# from math import prod

# def tuple_ops(my_tuple):
#   return(sum(my_tuple), prod(my_tuple))

# print(tuple_ops(integers))

# given_tuple = (1,2,3,4,5)
# a, b, c, d, e = given_tuple
# print(a,b,c,d,e) 


# ## sets
# my_set = {1,2,3,4,5}
# my_set.add(6)
# my_set.remove(3)

# print(my_set)

# def set_ops(set1, set2):
#   print(f'Union: {set1 | set2}')
#   print(f'Intersection: {set1 & set2}')
#   print(f'Difference: {set1 - set2}')
#   print(f'SymmDiff: {set1 ^ set2}')

# set_ops(set1={1,2,3,4,5}, set2={1,3,5,7})


## Dictionary: mutable unordered collection of keyvalue pairs, each key must be unique and values can be of any type.

# creating a dictionary
# student = {
#   "name": "Sabin",
#   "age": 19,
#   "course": "Python"
# }

# print(student)

# # two ways of acessing key value from a dictionary
# print(student['name'])
# print(student.get('age'))

# # .get method is more efficient as it avoids errors for missing keys.
# # print(student['grades']) (error)
# print(student.get('grades', "Not Found"))

# # adding and updating entriess
# student['grade'] = 'A' # add
# student['age']  = 12 # modify
# print(student)

# #deleting entries from a dict
# del student['grade']
# print(student)


# # iterating through dictionaries:
# for key in student:
#   print(key, student[key])

# # visulising what these methods return,
# print(student.items())
# print(student.values())

# for key, value in student.items(): 
#   print(f'{key}: {value}')

# for value in student.values():
#   print(value)

# # comoon dict methods

# #Keys and values:
# print(student.keys())
# print(student.values())

# # checking existence
# print("name" in student)
# print("grade" in student)


# # clearing all entries:
# student.clear()
# print(student)

# #nested discts:

# school = {
#   "class1" : {
#     "teacher" : "Mr. A", 
#     "students" : 30
#   },
#   "class2" : {
#     "teacher" : "Mr. B", 
#     "students" : 25
#   }
# }

# print(school['class1']['teacher'])



## Practice problems

#1
fruits= {
  "apple": 100,
  "banana" : 50,
  "cherry": 75
}


fruits['date'] = 120
fruits['apple'] = 110

del fruits['banana']

print(fruits)

#2
for key, value in fruits.items():
  print(f'{key}: {value}')

#3
# def string_to_dict_acc_to_freq(my_string):
#   # new_string =  my_string.lower().split(' ')
#   # print(new_string)
#   words = {}
#   for word in new_string:
#     if word in words:
#       words[word] = words.get(word) + 1
#     else:
#       words[word] = 1
#   return words

def string_to_dict_acc_to_freq(my_string):
  words = {}
  for word in my_string.lower().split(' '):
    words[word] = words.get(word, 0) + 1
  return words


print(string_to_dict_acc_to_freq('Hello world hello'))


#4

library = {
    "Fiction": {"books": ["1984", "Brave New World"], "count": 2},
    "Non-Fiction": {"books": ["Sapiens", "Educated"], "count": 2}
}

library['Fiction']['books'].append('Summer Love')
print(library['Fiction']['books'])
library['Fiction']['count'] = len(library['Fiction']['books'])

print(library)



#5
teacher = {
  "name": 'Sabin',
  "salary": 100000,
}

student = {
  "name": "Yaman",
  "age": 19
}

# adds the key value pair of students into teacher, and if found similar keys, student wala will overwrite
teacher.update(student)
# merged = {**teacher, **student}
merged  = teacher | student

# result
print(teacher)
print(merged)
















