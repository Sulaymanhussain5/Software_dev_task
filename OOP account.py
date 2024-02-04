from datetime import date #Imports the date and time module, so the programme will add the dates 

import random #Imports the random module, to radomised integers


class Account: #Class Account handles the default, get and set interest rate, date, deposit and withdraw functions.
    
    def __init__(self, ID, accountBalance, annualInterestRate, accountStartUpDate): #Init function refers to these object, by using a "self".
        
        self.ID = ID #self variable that refers to Account ID
        
        self.accountBalance = accountBalance #self variable that refers to balance of your account
        
        self.annualInterestRate = annualInterestRate #self variable that refers annual interest rate
        
        self.accountStartUpDate = accountStartUpDate #self variable that refers to dates
        

    def default(self): #default function, create a default of each object
        
        self.ID=0 #Default of "ID"
        
        self.accountBalance = 0 #Default of "accountBalance"
        
        self.annualInterestRate = 0 #Default of "annualInterestRate"
        
        self.accountStartUpDate = date.today() #Default of "accountStartUp"
        

    def createAccount(self): #createAccount (VOID) function that gives ID to users if they don't have a account and let user inputs their initial balance
        
        haveAccount=input("Do you have an account?:") #String data type to ask user if they have an account
        
        if haveAccount == "Yes": #If they have an account then it will print out their details of their account.

            print("") #Gives more space
            
            print("------------------Your account------------------") #Displays this message when user says yes
            
            print(self.accountBalance) #Prints the "accountBalance"
            
            print(self.accountStartUpDate) #Prints the "accountStartUpDate"
            
            print(self.annualInterestRate) #Prints the "annualInterestRate"
            
            
        else:
            createMyAccount=input("Would you like to have an account?:") #String date type to ask user if they would like to have an account.
            
            if createMyAccount == "Yes": #If yes, then it will ask for users name, there budget and give them random ID number.

                print("") #Gives more space

                print("-----------------Sign up-----------------")

                print("") #Gives more space
                
                name=input("Enter your name:") #String data type to ask user for their name
                
                balance=float(input("Enter your budget?:")) #Float data type to ask user for their balance
                
                self.accountBalance=balance #By using self, it will refer the accountBalance which is in the class to "balance"
                
                print("Name:" + name) #Prints there name
                
                print("Your Balance" , balance) #prints there balance
                
                id=random.randint(1000,5000) #Randomised the ID starting from 1000 to 5000
                
                print("ID:",id) #Prints there ID
                
                return name,balance,id #Returns these variables
            else:
                exit() #Programme crashes if they say no
                


    def getInterestRate(self): #getInterestRate (VOID) function that collects the annualInterstRate from the class
        
        return self.annualInterestRate #Returns the class annualInterestRate
    

    def setInterestRate(self): #setInterestRate (VOID) function that set the interest rate.
        
        interestR=random.randint(1.0,9.0) #Randomised the interest rate starting from 1.0 to 9.0
        
        print("Interest Rate: %",interestR) #Prints the interest rate
        
        return interestR #Returns the interest rate
    


    def date(self): #date funtion that creates the date of when the account was created.
        
        print("Date created:" , date.today()) #Prints the dates
        


    def getMonthlyInterestRate(self): #getMonthlyInterestRate (VOID) funtion that calculates monthly interest rate to their balance
        
        interestR=random.randint(1.0,9.0) #Randomised the interest rate starting from 1.0 to 9.0

        print("Monthly rate:%" ,interestR)
        
        r = self.accountBalance/12 * interestR  #Formular on calculating the monthly interest rate

        print("Your monthly interest rate is:" ) #Prints the monthly interest rate


        print(round(r)) #Rounds integers when given long integers
        
        
        return r #Returns the monthly interest rate
    

    def withdraw(self): #Withdraw function that lets user to withdraw their balance

        print("") #Gives more space

        print("--------------------Withdraw--------------------")
        
        wit=float(input("How much you want to withdraw?:")) #Float data type that asks user how much they wanr to withdraw there budget
        
        take=self.accountBalance - wit #Formula on withdrawing the budget
        
        self.accountBalance = take #Refering to class accountBalance which is assign to wit
        
        print("Budget after withdrawn:", take) #Prints budget after withdraw
        


    def deposit(self): #Deposit function that lets user to deposit their balance

        print("") #Gives more space

        print("---------------------Deposit---------------------")
        
        d = float(input("How much money you want to deposit?:")) #Float data type that asks user how much they wanr to deposit there budget
        
        cal = self.accountBalance + d #Formula on depositing the budget

        self.accountBalance = cal

        
        print("Your budget after deposited:" , cal) #Prints budget after deposit

         

        
    


    
        
        


     
        

                  
                
                          

account=Account(1122,20000,4.5,6) #Closes the class, inside the bracket is refering to the object that the programe wants to print out.


#Closes the function
#------------------------------
account.createAccount()
account.setInterestRate()
account.date()
account.getMonthlyInterestRate()
account.withdraw()
account.deposit()
#------------------------------

        





    
        


        

 



        

        

        
        
        


        
    
