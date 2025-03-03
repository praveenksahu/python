#Dictionary in Python

#Method1
# my_dict = {'key':'value', 'key1':'value1'}
my_dict = {'Name':'Aarya','Class':'8','Age':'13'}
print(my_dict)
print(type(my_dict))

#Method 2
# using dict const
my_dict_const = dict(Name = 'Shreeja',Class=8,Age=5)
print(my_dict_const)
print(type(my_dict_const))

#Method 3
# using list of tuples
my_dict_const_lt=dict([('Name','Aman'),('Age','30'),('Class','ME')])
print(my_dict_const_lt)
print(type(my_dict_const_lt))

#Adding a new key value pair
my_dict_const_lt['Email']="aman@gmail.com"
print(my_dict_const_lt)

#Modify an item
my_dict_const_lt["Email"]="aman@example.com"
print(my_dict_const_lt)

#Values
print(my_dict_const_lt.values())

#Keys
print(my_dict_const_lt.keys())

#Items - List of tuples
print(my_dict_const_lt.items())

#Get method - if value not found then it will give the string message.
print(my_dict_const_lt.get('test',"Value not found"))

#Nested Dictionary
students = {"student1":{
    "name": "Rajan",
    "city":"Ranchi",
    "email":"rajan@abc.com"
},"student2":{
    "name": "Amit",
    "city":"Pune",
    "email":"amit@abc.com"
}}
print(students["student1"])

#for loop for keys and values
for keys,value in students.items():
    print(keys,value)

print("****************")

for keys in my_dict_const_lt.keys():
    print(keys)

for val in my_dict_const_lt.values():
    print(val)

print("****************")

print(students)
print(students["student1"])
print(students["student2"])
