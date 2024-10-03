# Sub Classes
class Person:
    def __init__(murderer, suspect):
        murderer.suspect = suspect
        
class Room:
    def __init__(murderer, room):
        murderer.room = room
        
class Room_Value:
    def __init__(murderer, room_value):
        murderer.room_value = room_value
        
class Tool:
    def __init__(murderer, tool):
        murderer.tool = tool
        
class Tool_Value:
    def __init__(murderer, tool_value):
        murderer.tool_value = tool_value
        
# Main Class inheriting all the subclasses
class Scenario(Person, Room, Tool):
    def __init__(murderer, suspect, room, tool):
        Person.__init__(murderer, suspect)
        Room.__init__(murderer, room)
        Tool.__init__(murderer, tool)

# Registering the Suspects using Object
Suspect1 = Scenario(suspect="John", room="Bathroom", tool="Lead Pipe")
Suspect2 = Scenario(suspect="Cathy", room="Dining", tool="Revolver")
Suspect3 = Scenario(suspect="Cathy", room="Ball", tool="Dagger")
Suspect4 = Scenario(suspect="Samuel", room="Master Bedroom", tool="Revolver")
Suspect5 = Scenario(suspect="John", room="Kitchen", tool="Dagger")
Suspect6 = Scenario(suspect="Cathy", room="Master Bedroom", tool="Hammer")     

# Returns the real name of the value
# For Example: Original_Room1 will print "Bathroom" str
Original_Room1 = Suspect1.room
Original_Room2 = Suspect2.room
Original_Room3 = Suspect3.room
Original_Room4 = Suspect4.room
Original_Room5 = Suspect5.room
Original_Room6 = Suspect6.room

# Adding value to the rooms
Room1 = Room_Value(room_value=0.3)
Room2 = Room_Value(room_value=0.9)
Room3 = Room_Value(room_value=0.5)
Room4 = Room_Value(room_value=0.3)
Room5 = Room_Value(room_value=0.1)
Room6 = Room_Value(room_value=0.3)

# Changing the value of "Bathroom" str to 0.3 int
Suspect1.room = Room1.room_value
Suspect2.room = Room2.room_value
Suspect3.room = Room3.room_value
Suspect4.room = Room4.room_value
Suspect5.room = Room5.room_value
Suspect6.room = Room6.room_value

# Returns the real name of the value
# For Example: Original_Tool1 will print "Lead Pipe" str
Original_Tool1 = Suspect1.tool
Original_Tool2 = Suspect2.tool
Original_Tool3 = Suspect3.tool
Original_Tool4 = Suspect4.tool
Original_Tool5 = Suspect5.tool
Original_Tool6 = Suspect6.tool

# Adding value to the tools
Tool1 = Tool_Value(tool_value=0.1)
Tool2 = Tool_Value(tool_value=0.7)
Tool3 = Tool_Value(tool_value=0.4)
Tool4 = Tool_Value(tool_value=0.7)
Tool5 = Tool_Value(tool_value=0.4)
Tool6 = Tool_Value(tool_value=0.8)

# Changing the value of "Lead Pipe" str to 0.1 int
Suspect1.tool = Tool1.tool_value
Suspect2.tool = Tool2.tool_value
Suspect3.tool = Tool3.tool_value
Suspect4.tool = Tool4.tool_value
Suspect5.tool = Tool5.tool_value
Suspect6.tool = Tool6.tool_value

# Adding up the room value and tool value
# For Example: Calculate1 is 0.3 + 0.1 = 0.4
Calculate1 = Suspect1.room + Suspect1.tool
Calculate2 = Suspect2.room + Suspect2.tool
Calculate3 = Suspect3.room + Suspect3.tool
Calculate4 = Suspect4.room + Suspect4.tool
Calculate5 = Suspect5.room + Suspect5.tool
Calculate6 = Suspect6.room + Suspect6.tool

# Checks the highest Calculate by using max()
Total_Value = max(Calculate1, Calculate2, Calculate3, Calculate4, Calculate5, Calculate6)

# Checks who is the highest suspect's value by using if, elif, else
if Total_Value == Calculate1:
    Winner = Suspect1
elif Total_Value == Calculate2:
    Winner = Suspect2
elif Total_Value == Calculate3:
    Winner = Suspect3
elif Total_Value == Calculate3:
    Winner = Suspect3
elif Total_Value == Calculate4:
    Winner = Suspect4
else:
    Winner = Suspect5

# Displaying the Task Name and Number
print("Task 1: Detective")
# Returning all of the Suspect's Name, Room, Tool and their Value
print(f"{Suspect1.suspect} \t| {Original_Room1} = {Suspect1.room} \t| {Original_Tool1} = {Suspect1.tool}")
print(f"{Suspect2.suspect} \t| {Original_Room2} = {Suspect2.room} \t\t| {Original_Tool2} = {Suspect2.tool}")
print(f"{Suspect3.suspect} \t| {Original_Room3} = {Suspect3.room} \t\t| {Original_Tool3} = {Suspect3.tool}")
print(f"{Suspect4.suspect} \t| {Original_Room4} = {Suspect4.room} \t| {Original_Tool4} = {Suspect4.tool}")
print(f"{Suspect5.suspect} \t| {Original_Room5} = {Suspect5.room} \t| {Original_Tool5} = {Suspect5.tool}")
print(f"{Suspect6.suspect} \t| {Original_Room6} = {Suspect6.room} \t| {Original_Tool6} = {Suspect6.tool}")
# Says the winner above in the if, elif, else and printing the total value and their name
print("\nQUESTION: Who has the highest value among the suspects?")
print(f"ANSWER: The suspect is likely to be {Winner.suspect}, with a value of: {Total_Value}!\n")