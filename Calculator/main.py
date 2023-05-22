import os #importing os library to clear the console when i want
from art import logo

def clear(): #the console cleaner function
    os.system('cls' if os.name == 'nt' else 'clear')


def add(number1,number2): 
    """adding function, adding first parameter with second parameter"""
    return number1 + number2
    
def subtract(number1,number2): 
    """subtracting function, subtract the first parameter from the second parameter"""
    return number1 - number2
    
def multiply(number1,number2):
    """multiplying function, multiply the first parameter with second parameter"""
    return number1 * number2
    
def divide(number1,number2):
    """dividing function, divide the first parameter from the second parameter"""
    return number1 / number2

#operations dic, if the user call "+" (add function) will appear etc. 
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): #main function 
    print(logo) #printing the logo of the program from art.py
   
    num1 = float(input("What's the first number?: ")) 

    #printing the all symbols in operations dic
    for symbols in operations:
        print(symbols)

    should_continue = True #flag
    while should_continue:
        
        operations_symbol = input("pick an operation: ") #picking the symbol that i want
        num2 = float(input("What's the next number?: ")) #the next number 
        #the result, going to the operation dic then -> number 1 (+,-,*,/,acctuly i put what i want here like radical or power etc.) number 2
        result = operations[operations_symbol](num1,num2) 
        print(f"{num1} {operations_symbol} {num2} = {result}")
        
        user_status = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if user_status == "y":
            should_continue = True #pick a new operation system again
            num1 = result #now the old result equal to number1, no not mohamed ramadan ha ha funny >_<
        elif user_status == "n":
            should_continue = False
            clear() #clear the console
            calculator() #calling the function again to be like infinite loop
        else:
            print("Bye Bye")
            return #pause the game
            
calculator()
