#Imports a module that allows the python to run library that includes maths.
import math

#First function which collects the answer for weights and heights
def collectingWeightHeight():
    
    weight=float(input("Insert your weight in kg:")) #Data type of float that collects the weight of the user
    
    height=float(input("Insert your height in m :")) #Data type of float that collects the height of the user
    
    total=weight/(height**2) #Formula to calculate the weight and the height based on users response
    
    print(round(total)) #Rounds the answer


#Second function to give the result of users health based on their result
def result():
    
    my_result=float(input("Insert your result to find out your health:")) #Data type of float that collects the total of height and weight
     
    if my_result <18.5: #If the result is less than 18.5 then print "underweight"
        
        print("UNDERWEIGHT") #It prints "underweight"
        
    elif my_result >=18.5 and my_result <=24.9: #If the result is less than equal to 24.9 then print "Normal weight"
        
        print("NORMAL WEIGHT") #It prints "Normal weight"
        
    elif my_result >=25 and my_result <=29.9: #If the result is less than equal to 29.9 then print "Overweight"
        
        print("OVERWEIGHT") #It prints "Overweight"
        
    elif my_result >31: #If the result is greater than 31 then print "Obese"
        
        print("OBESE") #It prints "obese"
    else:
        print("You need to train") #If none of these has been entered then this will be printed


#Closes the two function
#-----------------------------
collectingWeightHeight()
result()
#-----------------------------

                
