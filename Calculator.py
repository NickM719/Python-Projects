#Mode Selection
mode = input("Simple or Precise: ")
#Read and Compute Inputs
def sum(a, b, sign):
    if sign == "+" or "add":
        return (int(a) + int(b))
    if sign == "-" or "subtract":
        return (int(a) - int(b))
    if sign == "*" or "Multiply":
        return(int(a) * int(b))
    if sign == "/" or "divide":
        return(int(a) / int(b))
#Get Inputs
a = input("Number 1: ")
b = input("Number 2: ")
c = input("Sign: ")
#Display Output
if mode == "Precise":
    print(f"The Output is {sum(a, b, c)}.")
else:
    print(f"{sum(a, b, c)}")