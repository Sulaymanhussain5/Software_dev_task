counter = 0 #Count variable is where it adds number of votes in each names



vote = True #Defining the while loop variable



#Adds names in the list
#-----------------------------------
addCandi1 = [] 
addCandi2 = []
addCandi3 = []
addCandi4 = []
#-----------------------------------


#Adds the number of votes in the list of participants
#-----------------------------------
namesAmount1 = 0 
namesAmount2 = 0
namesAmount3 = 0
namesAmount4 = 0
#-----------------------------------


voters_id = [1,2,3,4] #To start the vote with ID voters

print("-----------------Add your 4 participants-----------------")
print("")
names1 = input("Add list of name 1 here:") #Adds participant 1 in the voting system
names2 = input("Add list of name 2 here:") #Adds participant 2 in the voting system
names3 = input("Add list of name 3 here:") #Adds participant 3 in the voting system
names4 = input("Add list of name 4 here:") #Adds participant 4 in the voting system


while vote == True: #Starts the while loop
    
    print("") #Gives white space
    
    voteAccept = int(input("Vote ID 1-4 here:")) #String data type that let users put there voters ID
    
    if vote in voters_id: #If statement to show what happens if vote ID added
        
        print("You can now vote!!!")
        
        voters_id.remove(voteAccept) #Removes the ID number from the list
        
        print("") #Gives white space
        
        print("*******************************") 
        
        print("LIST OF PARTICIPANTS AND THERE NUMBERS")
        
        print("")

        #Prints list of added participants and there numbers
        #-----------------------------------------------------
        print("Press 1 to vote for", names1)
        print("Press 2 to vote for", names2)
        print("Press 3 to vote for", names3)
        print("Press 4 to vote for", names4)
        print("*******************************")
        #-----------------------------------------------------
        print("")


    print("VOTES BEGINS") 
    print("")
    print("**********************************************")
    vote = int(input("Enter your number here:")) #This is where users can vote
    
    if vote == 1: #If they press one, then names1 variable will be added to addCandi1 list
        
        addCandi1.append(names1) #names1 gets added to addCandi1 list
        
        namesAmount1 = namesAmount1 + 1 #Per 1 points get added every time they have voted by this name 
        
        print("Thank you for voting")

        

    elif vote == 2: #If they press Two, then names2 variable will be added to addCandi2 list
        
        addCandi2.append(names2) #names2 gets added to addCandi2 list
        
        namesAmount2 = namesAmount2 + 1 #Per 1 points get added every time they have voted by this name
        
        print("Thank you for voting")

        

    if vote == 3: #If they press Three, then names3 variable will be added to addCandi3 list
        
        addCandi3.append(names3) #names3 gets added to addCandi2 list
        
        namesAmount3 = namesAmount3 + 1 #Per 1 points get added every time they have voted by this name
        
        print("Thank you for voting")

        

    if vote == 4: #If they press Four, then names4 variable will be added to addCandi4 list
        
        addCandi4.append(names4) #names4 gets added to addCandi2 list
        
        namesAmount4 = namesAmount4 + 1 #Per 1 points get added every time they have voted by this name
        
        print("Thank you for voting")

    

   

    

    cont = input("Would you like to continue?:") #Middle of the while loop, this question will be asked
    
    if cont == "Yes": #If they say yes, then loop continues
        
        vote = True #Loop continues
        
    else:
        vote = False #Loop ends



#The result of voters in each names
#------------------------------------------------

print("-----------------------RESULT-----------------------")
print("")

print(names1,"has",namesAmount1, "Votes" )
print(names2,"has",namesAmount2, "Votes" )
print(names3,"has",namesAmount3, "Votes" )
print(names4,"has",namesAmount4, "Votes" )
#------------------------------------------------




#Gives winners to participants based on their points
#-------------------------------------------------------------------
print("***********************************************")
if namesAmount1 > namesAmount2:
    print("Winner is", names1)
elif namesAmount1 > namesAmount3:
    print("Winner is", names1)
elif namesAmount1 > namesAmount4:
    print("Winner is", names1)


elif namesAmount2 > namesAmount1:
    print("Winner is", names2)
elif namesAmount2 > namesAmount3:
    print("Winner is", names2)
elif namesAmount2 > namesAmount4:
    print("Winner is", names2)


elif namesAmount3 > namesAmount1:
    print("Winner is", names3)
elif namesAmount3 > namesAmount2:
    print("Winner is", names3)
elif namesAmount3 > namesAmount4:
    print("Winner is", names3)


elif namesAmount4 > namesAmount1:
    print("Winner is", names4)
elif namesAmount4 > namesAmount2:
    print("Winner is", names4)
elif namesAmount4 > namesAmount3:
    print("Winner is", names4)

#-------------------------------------------------------------------
    

   

