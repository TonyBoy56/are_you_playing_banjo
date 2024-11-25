# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

my_name = "Richard"
my_name2 = "Timothy"

def are_you_playing_banjo(name):
    if my_name[0] == "R" or my_name[0] == "r":
        print(f"{my_name } plays banjo")
    else:
        print(f"{my_name} does not play banjo")
    
are_you_playing_banjo(my_name)