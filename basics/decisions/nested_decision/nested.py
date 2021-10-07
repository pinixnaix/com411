# Asks the user to enter the type of book cover

print("What type of cover does the book have?")
cover = str(input()).lower()

if cover == 'soft':
    print("Is the book perfect-bound?")
    bound = str(input()).lower()
    if bound == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books!")
else:
    print("Books with hard covers can be more expensive!")
