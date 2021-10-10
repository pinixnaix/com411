print("How many cables should i avoid?")
cables = int(input())
x = 0
print("")
while x < cables:
    print("Avoiding ...", end="")
    x += 1
    print(f"Done! {x} live cables avoided.")
print("\nAll live cables have been avoided.")

