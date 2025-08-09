# variable
# integer is of two types. they are primitive and non-primitive

# primitive data type
# integer
a = 10
b = 15
c=a+b
print (c)

# string
a = "divya "
print(a)

# float

a = 5.5
b = 2.5
c = a + b
print(c)

# boolean
a = 1
print(bool(a))

a = 0
print(bool(a))

# non primitive data type

# list
# tuple
# set
# dictionary

listd = [1,2,3,4]
listd1 = ["a",1,2,3,4]
print(listd)
print(listd1)

tupled = (1,2,3,4)
tuplei = ("d","i","v",1,2,3)
print(tupled)
print(tuplei)

setd = {1,2,3,4}
print(setd)

dictionary1 = { "Name" : "Divya","Age" : 29,"Location" : "Perambur"}
print(dictionary1)

# List.append - This will add the mentioned number at the last position that also only one number at a strecth

list1 = [1,2,3,4]
list1.append(100)
print(list1)
list1.append(200)
print(list1)

# List.insertion - This will add the mentioned number at the given index position
list1 = [1,2,3,4]
list1.insert(2,102)
print(list1)
list1.insert(4,104)
print(list1)

# List.remove - This will remove the mentioned number from the space

list1 = [1, 2, 102, 3, 104, 4]
list1.remove(102)
print(list1)

list1.remove(104)
print(list1)

# list.pop - This will remove the position (index)

list1 = [1,3,5,7,9]
list1.pop(4)
print(list1)
list1.append(103)
list1.append(105)
print(list1)

# list.sort - This will sort the given list of numbers in ascending order
list2 = [1,9,4, 3,8, 5, 7, 123,103, 105]
list2.sort()
print(list2)


#list.sort(reverse = true)
list2 = [1,9,4, 3,8, 5, 7, 123,103, 105]
list3 = [2,4,3,7,5,8,6,9,12]
list2.sort(reverse = True)
print(list2)
print(list3)
list3.sort(reverse = True)
print(list3)

# list.count - This is used the find the count
listd = [1,5,5,3,5,7,8,23,43,45]
print(listd.count(5))

# list.index - this will give the index of that number
listd = [1,5,5,3,5,7,8,23,43,45]
print(listd.index(43))

#list.copy
listd = [1,5,5,3,5,7,8,23,43,45]
lists = listd
listd[4] = 100
print(listd)
print(lists)

# to see the memory of the stored decimal
listd = [1,3,5,7,9,11,13,5,17]
print(id(listd))

# list.clear - it will clear the values in the given list
listd = [1,3,5,7,9,2,4,6,8,]
listd.clear()
print(listd)

# list.extent - this command will merge both values as shown below
list1 = [1,3,5,7,9]
list2 = [2,4,6,8,0]
list1.extend(list2)
print(list1)

# ~~~~~
# tuple
# ~~~~~

# two types of tuples are there they are
# count and index

# count - This will mention us how many count of the mentioning numbers 

tuple1 = (1,2,5,3,5,3,4,5)
print(type(tuple1))

tuple1.count(5)
print(tuple1.count(5))

# in the above line we requested to get the count of that number which we have assigned "5"

tuple1 = (1,2,5,3,5,3,4,5)
print(tuple1.index(2))
print(tuple1.index(5))

# ~~~
# Set
# ~~~

setd = {1,3,5,2,4,6,8,0,7}
print(setd)

setd.add(200)
setd.add(300)
setd.add(400)
print(setd)

setd = {0,1,2,3,4,5,6,7,8,9,0,200,300,400}
setd.remove(200)
print(setd)
setd.remove(300)
print(setd)

# ~~~~~~~~~~~~~~~~~~~~
# union & intersection
# ~~~~~~~~~~~~~~~~~~~~

setd = {0,1,2,3,4,5,6,7,8,9,0,200,300,400}
sets = {12,13,14,15,16,17,18,19,1}
print(setd.union(sets))
print(setd.intersection(sets))
print(setd.difference(sets))

# ~~~~~~~~~~ 
# dictionary
# ~~~~~~~~~~

dict1 = {
    "Name" : "Sanjiv",
    "Couse" : "Data analyst",
    "Institute" : "Besant"
        }

# ~~~~~~~~~~~~~~~~~
# dictionary.update
# ~~~~~~~~~~~~~~~~~

list1 = [2,4,6,8,10,12,14,16,18]
list1.append(200)
print(list1)
# list2.insert(2,400)
# print(list2)
# need to confirm why the list count got decreased.
list1.remove(10)
print(list1)
list1.pop(2)
print(list1)
list1.pop()
print(list1)
list1.sort()
print(list1)


list1 = [3, 1, 4, 2]
list1.sort(reverse=True)
print(list1)
list1.sort()
print(list1.sort)











