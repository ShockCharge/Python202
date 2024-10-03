# List of emojis
emojis = {
    "Soccer": "\u26BD",
    "Cricket": "\U0001F3CF",
    "Rugby": "\U0001F3C9",
    "Golf": "\u26F3",
    "Volleyball": "\U0001F3D0",
    "Hockey": "\U0001F3D2",
    "Squash": "\U0001F3BE",
    "Bowling": "\U0001F3B3",
    "Table-Tennis": "\U0001F3D3",
    "Handball": "\U0001F3C0",
    "Basketball": "\U0001F3C0",
    "Boxing": "\U0001F94A"
}

# Intro Message
print("Task 2: Sports Emojis")
print("\nType the name of the emoji in the list provided,")
print("and you can separate them using commas \",\" symbol.")

# Print the list of emojis as a demo/example that user can look at and copy the keyword
print("\nSoccer = \u26BD")
print("Cricket = \U0001F3CF")
print("Rugby = \U0001F3C9")
print("Golf = \u26F3")
print("Volleyball = \U0001F3D0")
print("Hockey = \U0001F3D2")
print("Squash = \U0001F3BE")
print("Bowling = \U0001F3B3")
print("Table-Tennis = \U0001F3D3")
print("Handball = \U0001F3C0")
print("Basketball = \U0001F3C0")
print("Boxing = \U0001F94A")

input = input("\nEnter emojis: ")
keyword = input.split(",")

def check_input():
    if len(input) < 5:
        print("ERROR! You entered less than 5 emojis!")
    else:
        return input
    
input = check_input()

for entry in keyword:
    entry = entry.strip()
    grab_emoji = emojis.get(entry, "?")
    print(grab_emoji)
