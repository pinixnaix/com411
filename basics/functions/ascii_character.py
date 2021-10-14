print("Program Started!")
print("Please enter an ASCII code:")

code = int(input())

if code in range(32, 127):
    print(f"The character represented by the ASCII code {code} is ", chr(code))
else:
    print("!!ERROR!! ASCII code not in range!!")
print("Program Ended!")
