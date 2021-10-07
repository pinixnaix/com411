# Asks the user to enter an activity

print("Please enter the activity to be performed.")
activity = input().lower()

if activity == 'calculate':
    print("\nPerforming calculations...")
else:
    print("\nPerforming activity...")

print("\nActivity completed!")
