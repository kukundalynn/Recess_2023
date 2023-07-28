#control flow
#if clause
#if condition 1:
#print("true")

#input
#age=int(input())
#if age<18:
#print("You are underage")
#elif age >=18 and age<65:
    #print("you are an adult")
    #else:
        #print("you are a senior citizen")

#have a variable 
#age=45 
#if age<18:
    #print("you are underage")
    #elif age>=18 and age<65:
        #print(" you are an adult")
        #else:
            #print("you are a senior citizen")

#loops
#cars=["tesla","jeep","ford","toyota","BMW"]
#for car in cars:
    #print (car)

 #fruits=["grapes","apples","kiwi","mango"]   
 #for fruit in fruits
    #print(fruit)

  #fruits_count=0
  #while fruits_count< len(fruits)  
    #print(fruits_count)
    #fruits_count+=1

#x=0
#while x<10 and x>2:
    #print(x)
    #if x==8:
        #break
   # x+=1

 #break and continue statements 
 #break terminates loop
 #for number in range(1,8)
    #if number==4:
     #   break
   # print(number) 

 #continue skips the number 
 #for number in range(1,8)
   # if number==4:
      #  continue
    #print(number)

#Exception handling(try,except, finally)
#try:
   # x = 10/0
    #except ZeroDivisionError:
       # print("error: cant be divided by zero")
    #finally:
       # print("this is always divided") 

#example
#try:
  #print(x)
#except:
  #print("Something went wrong")
#finally:
  #print("The 'try except' is finished")

#exercise
health ={
         1: 'Im very sick',
         2: 'Im sick',
         3: 'Im in alot of pain',
         4: 'Im in pain',
         5: 'Im fair',
         6: 'Im okay',
         7:  'Im good', 
         8: 'Im very good',
         9: 'Im great',
         10: 'Im strong',
}
#prompt
user_health = input("On the scale of 1-10, how are you feeling")
if int(user_health) in health:
    print(health[int(user_health) ])
else:
    print("im sorry we dont understand")    

