"""
x= 12
print(type(x))
y ="hello"
z= 1j
print(type(y))
print(type(z))
# lists (ordered, changeable and take duplicate values)
#Afternoon= ["Trevor","Peter", "Blessing"]
Afternoon=["Trevor", "Peter", "Blessing","Trevor", "Trevor","Blessing"]
print(Afternoon)
print(len(Afternoon)) #length of list
print(type(Afternoon)) #type of datatype
#access list items
print(Afternoon[2])
print(Afternoon[-3])
#accessing a range of items
print(Afternoon[3:6])
print(Afternoon[:5])
print(Afternoon[1:])
#add using append
Afternoon.append('Martha')
print(Afternoon)
#add using insert
Afternoon.insert(0,"livingstone")
print(Afternoon)
#remove from list using index
Afternoon.pop(6)
print(Afternoon)



#Tuples ( store items in a single variable)
# Tuples are ordered and unchangeable

phones=("samsung","iphone","tecno")
print(phones)

#allow for duplicate values
#access tuples

print(phones[0])
print(phones[2])

#add items to tuple (convert to a list)
z=list(phones)
z.append("nokia")
phones= tuple(z) #converting back to a tuple
print(phones)

#for loop
#for y in phones
#print(y)

#sets
#store multiple items in asingle variable
#unchangeable but can add and remove
#no duplicates

setone={"matooke","rice","irish"}
print(setone)

#length of set
print(len(setone))

#datatype
print(type(setone))

#accessing item in set
print("matooke" in setone)

#add items
setone.add("yam")
print(setone)

#adding 2 sets
set1={"water","soda"}
set2= setone.union(set1)
print(set2)
"""
#dict#ionary dict
#used to store values in key:values pairs
#are ordered, changeable but dont allow duplicates 

mydict={
    "phone":"iphone",
    "iphonemodel": 15,
    "year": 2015

}
print(mydict)
#length of a dict
print(len(mydict))
#datatype
print(type(mydict))
#accessing dictionary items 
z = mydict["year"]
print(z)
y = mydict.get("iphonemodel")
print(y)
w = mydict.keys()
print(w)

#Ex.1 values()method to return a list of items in the dictionary


#Ex.2 check if key exists
if "phone" in mydict:
    print("this will execute")

else:
    print("this will not")

#Ex.3 update
mydict['phone']  =  "Nokia"
print(mydict['phone'])

#Ex.4 add and  remove
#remove
mydict.pop("year")
print(mydict)
#add
mydict.update({"Company": "Apple"})
print(mydict) 

#Ex.5 nest dictioaries
students = {}  # Creating parent dictionary

students["std1"] = {}   # Creating std1 child dictionary
students["std2"] = {}    # Creating std2 child dictionary

students["std1"]["Name"] = "Pete"     # Adding key value pair to std1
students["std1"]["Age"] = 16         # Adding key value pair to std1
students["std1"]["Marks"] = 45      # Adding key value pair to std1

students["std2"]["Name"] = "Mary"      # Adding key value pair to std2
students["std2"]["Age"] = 16           # Adding key value pair to std2
students["std2"]["Marks"] = 54        # Adding key value pair to std2


print(students)

#Numbers
# integer,float, complex

#conversion
w=10 #int
r=3.9 #float
s=2j #complex

z= complex(w) #int to complex 
print(type(z))

y=float(w)    #int to float
print(type(y))

z=complex (r)    #float to complex
print(type(z))

#Casting-specify variable type
#strings
 #Ex.1 Length
string = "Afternoon"
print(len(string))

#Ex.2 for loop 
for i in "Afternoon":
  print(i)

#Ex.3 slicing
slice = string[0:3] 
slice = string[0:-3] 
slice = string[:3] 
slice = string[::2]

#modify
a = "Afternoon"
print(a.lower())

print(a.upper())

#format strings-works when one wants to combine a string to a number 
age=23
name = "My name is Lynn and I am {}"
print(name.format(age))


#Boolean- true or false
#print(bool(12))
#exercise
def a_bigger(a, b):
  if a > b and (a - b) >= 2:
    return True
  else:
    return False





  