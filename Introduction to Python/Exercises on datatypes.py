#Exercise 1 LISTS
#1
names=["Lynn","Laura","Cronnie","Ivan","Ian"]
print(names[1])
#2
names.pop(0)
names.insert(0,"Angella")
#print(names)
#3
names.insert(5,"Ryan")
print (names)
#4
names.insert(2,"Bathel")
print(names)
#5
names.pop(2)
print(names)
#6
print(names[-1])
#7
Numbers=[1,2,3,4,5,6,7]
print(Numbers[2:5])
#8
Countries = ["Kenya", "Egypt", "Tz", "Uganda", "Sudan"]
Countries.copy()
  
#9
for i in Countries:
    print(i)

#10
animals=["dog","cat","mouse","antelope"]
animals.sort()   #ascending
print(animals)

animals.sort(reverse=True)  #descending
print(animals)

#11
check = 'A'
res = [idx for idx in animals if idx[0].lower() == check.lower()]
print(res)

#12
list1 =["Lynn"]
list2 =["Kukunda"]
list3 = list1 +list2
print(list3)

#Exercise 2 TUPLES
#1
phones= ("samsung" , "iphone", "tecno", "redmi")
print(phones[1])

#2
print(phones[-2])

#3
x=list(phones)
x.pop(1)
x.insert(1, "itel")
phones=tuple(x)
print(phones)

#4
z=list(phones)
z.append("Huawei")
phones= tuple(z)
print(phones)

#5
for y in phones:
    print(y)

#6
p=list(phones)
p.pop(0)
phones= tuple(p) 
print(phones)

#7
cities =("Kampala", "Entebbe", "Jinja")
print(cities)

#8
for i in cities:
    print(i)

#9
print(cities[1:5])

#10
tuple1=("Lynn")
tuple2=("Kukunda")
tuple3 =tuple1 + tuple2
print(tuple3)

#11
colours=("red","blue", "orange")
multiply= colours*3
print(multiply)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count8= thistuple.count(8)
print(count8)

#Exercise 3 SETS
#1
beverages={"soda","water","milk"}

#2
beverages.add("tea")
print(beverages)

#3
mySet = {"oven", "kettle", "microwave", "refridgerator"}
print("microwave" in mySet)

#4
mySet.remove("kettle")
print(mySet)

#5
for w in mySet:
    print(w)

#6
lista=[1,2,3,4]
seta={5,6}
l=set(lista)    
seta.union(l)
print(seta)

#7
age={21}
names={"lynn"}
names.union(age)


#Exercise 4 STRINGS
#1
str1= "hello"
int1= 21
print(str1.format(int1))

#2
txt = "Hello, Uganda!"
txt.strip()

#3
print(txt.upper())

#4
print(txt.replace("U", "V"))

#5
y="I am proudly Ugandan"
print(y[2:5])

#6
#x = "All “Data Scientists” are cool!"
x="All \"Data Scientists\" are cool!"
print(x)

#Exercise 5 Dictionaries
#1
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
z = Shoes["size"]
print(z)

#2
Shoes['Nick']  =  "addidas"
print(Shoes['brand'])

#3
Shoes.update({"type": "Sneakers"})
print(Shoes)

#4
w = Shoes.keys()
print(w)

#5
print(Shoes.values())

#6
if "size" in Shoes:
    print("this will execute")

else:
    print("this will not")

#7
for n in Shoes:
    print(n)

#8
Shoes.pop("color")
print(Shoes)        

#9
Shoes.clear()

#10
mydict={
    "phone":"iphone",
    "model": 15,
    "year": 2015

}
print(mydict)
mydict.copy()

#11
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