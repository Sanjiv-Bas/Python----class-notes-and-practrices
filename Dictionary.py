# In Python, a dictionary is a collection of key–value pairs that is unordered, mutable, and unique by keys.

dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1) 
# Result ==> {'Name': 'Divya', 'Age': 30, 'Location': 'Perambur'}


# Dictionary.get()
# we could get any particular key by giving the below code
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1.get("Name"))
# Result ==> Divya

# Dictionary.update()
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
dic1.update({ "Name" : "Divyasanjiv", "Location" : "Saidapet"})
print(dic1)
#  Result ==> {'Name': 'Divyasanjiv', 'Age': 30, 'Location': 'Saidapet'}

# Dictionary.pop()
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1.pop("Age"))
# Result ==> 30

# Dictionary.keys()
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1.keys())
# Result ==> (['Name', 'Age', 'Location'])

# Dictionary.values()
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1.values())
# Results ==> (['Divya', 30, 'Perambur'])

# Dictionary.items()
dic1 = { "Name" : "Divya", "Age" : 30, "Location" : "Perambur"}
print(dic1.items())
# Result ==>  ([('Name', 'Divya'), ('Age', 30), ('Location', 'Perambur')])