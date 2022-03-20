# Version 2.0.1
# 6 III 2022
print("To-Do list program, by Damian.\n")
todo = input("Input the path to the .txt file in which the todo list is saved\n")
print("Type /exit to exit.")
print("Type /erase to erase the list.")
print("Type /read to display the list")
x = True                                        # For the while loop
a = open(todo, "a")                             # Opens the file in append mode (adds stuff at the end of the file)
while(x == True):
    stuff = input()
    if(stuff.lower() == "/exit"):               # .lower() added so it's case insensitive
        a.close()                               # Closes the file
        x = False                               # End the program
        input("Press Enter to leave")
    elif(stuff.lower() == "/erase"):
        a = open(todo, "w")                     # Changes to write mode (overwriting the whole file)            
        a.write("")                             # Erases everything
        a = open(todo, "a")                     # Goes back to append mode
        a = open(todo, "w")
        a.write("")
        a = open(todo, "a")                     # Does it for the second time because it doesn't work the first time for some reason
        print("List erased.")
    elif(stuff.lower() == "/read"):
        a = open(todo, "r")                     # Changes to read mode
        print(f"To-Do list:\n{a.read()}")       # Prints the list
        a = open(todo, "a")                     # Back to append mode
    else:
        a.write(stuff+"\n")                     # Adds whatever the user writes at the end of the list and changes to the next line so everything is written in seperate lines
