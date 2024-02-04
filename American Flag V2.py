#Variables that represents the symbols that will be added to make american flag. "*" shows how many symbol will be added in one variable.
#--------------------------------------
stars="*" * 6
stars2="*" * 5
equals="=" * 33
equals2="=" * 34
equals3="=" * 40
#--------------------------------------



#Using a for loop, to list down symbols where it will design a american flag.
#range (1,10) = start the list from and and finish it to 9.
for i in range (1,10):
    
    if(i % 2 == 1): #If the symbol adds up the Odd numbers then print stars and equals.
        
        print(stars +  equals) #It prints the variables
        
    elif (i % 2 == 0): #If the symbol add up to even numbers, then it prints out stars 2 and equals 2.
        
        print(" " + stars2 + equals2) #It prints the variable 


for i in range (1,7): #Second for loop adds last 6 equals symbol to finish the american flag.
    
    print(equals3) #It prints the variable



    
