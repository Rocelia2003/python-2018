#rocelia tranquilino 08-30-18
import random 
my_list= [ "yes", "maybe","no", "that will never happen"]
 
  
name = input("what's your name?")

print( "Welcome " + name.title()) 

while True:
    user_input = input("What is your question? ")
    choice = random.choice(my_list)
    
