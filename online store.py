#Lists of products and their costs
#-------------------------------------------------------------------
products = ['Pencil Case', 'Calculator' , 'Ruler' , 'Highlighter']
costs = [5.00 , 15.00 , 10.00 ,2.00]
#-------------------------------------------------------------------




myCart=[] #Adds the chosen product in this list

myCost=[] #Adds the cost of the product to the list



print("-------------Welcome to Education Super Store-------------------")
print("")

print("----------------Available Items----------------")
print("")
print("Pencil Case - £5.00")
print("Calculator - £15.00")
print("Ruler - £10.00")
print("Highlighter - £2.00")

print("")


ask=input("Would you like order from ESS?:") #String data type variable that ask the user if they like to order

if ask=="Yes": #If they say yes then it will go to the while loop
    
    print("") #Prints nothing, instead it goes to the while loop
    
else:
    exit() #The program crashes when user does not want to order



orderAgain=True #By using True variable, it will loop customers orders until they descide to not order


counter=0 #Collects  is the quantity of customers orders


finalCost=0 #Collects the cost for each item



while orderAgain==True: #By using a while loop, it will continuesly ask user if they want to order, until they decide not to order.

    collect_order=input("Please insert your item of choice:") #String data type variable that lets users to input the item
    

    if collect_order=="pencil Case": #If user enters Pencil case, then it will be added to their cart and it's cost
        
        
        myCart.append(products[0])  #Collects the Pencil case in "products" list and adds it to "myCart" list
        

        myCost.append(costs[0]) #Collects Pencil case costs in "costs" list and adds it to the list

        counter=counter+1 #Adds the quantity of product

        finalCost=finalCost+(costs[0]) #Collects Pencil case cost in "costs" list and adds the Total costs for Pencil case.
        
        


    elif collect_order=="Calculator": #If user enters Caculator, then it will be added to their cart and it's cost
        
        myCart.append(products[1]) #Collects the Calculator in "products" list and adds it to "myCart" list
        
        myCost.append(costs[1]) #Collects Calculator costs in "costs" list and adds it to the list
        
        counter=counter+1 #Adds the quantity of product
        
        finalCost=finalCost+(costs[1]) #Collects Calculator cost in "costs" list and adds the Total costs for Calculator.
        


    elif collect_order=="Ruler": #If user enters Ruler, then it will be added to their cart and it's cost
        
        myCart.append(products[2]) #Collects the Ruler in "products" list and adds it to "myCart" list
        
        myCost.append(costs[2]) #Collects Ruler costs in "costs" list and adds it to the list
        
        counter=counter+1 #Adds the quantity of product
        
        finalCost=finalCost+(costs[2]) #Collects Ruler cost in "costs" list and adds the Total costs for Ruler.
        


    elif collect_order=="Highlighter": #If user enters Highlighter, then it will be added to their cart and it's cost
        
        myCart.append(products[3]) #Collects the Highlighter in "products" list and adds it to "myCart" list
        
        myCost.append(costs[3]) #Collects Highlighter costs in "costs" list and adds it to the list
        
        counter=counter+1 #Adds the quantity of product
        
        finalCost=finalCost+(costs[3]) #Collects Highlighter cost in "costs" list and adds the Total costs for Highlighter.


    else:
        
        print("This item is unavailable") #When customer says no, then it will leave this message.
    
    done = input("Have you finished? Y/N:") #String data type that asks users if they are done in ordering the item
    
    if done=="N": #Continue to loop when customers chose to not finish
        
        orderAgain=True #This continues the loop
    else:
        
        orderAgain=False #Loop ends when customers chose to finsih the order
        


    if counter >=4: #If the counter (quantity) is greater than 4, then the loop will end
        
        print("Sorry. Minimum of 4 items can be ordered") #Prints the message when user enters more than 4 items
        
        orderAgain=False #Ends the loop


print("Amount of ordered items:" , counter) #Prints out the quantity of the items         




x=0 #X is assign to 0, which it will be used to refer as amount of items and costs




#The receit
#--------------------------
print("     ")
print("My order list:")
print("**********")
#--------------------------




while x <counter: #By using a while loop, the programme will adds amount of items and cost, which will be added to give total cost.
    
    print("Items:" +(myCart[x])) #Amount of items they have ordered
    
    print("Costs £:" +str(myCost[x])) #+str converts the string to int, and it collects the total cost of the item
    

    
    x=x+1 #1 items and cost will be added when users chooses these items
    


#Total costs displayed
#-------------------------------------
print("                      ")
print("**************")
print("Total Cost£:" +str(finalCost)) #Gives you a final cost
print("**************")
#-------------------------------------





                  
                  
