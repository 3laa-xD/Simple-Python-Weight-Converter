# Python weight converter
weight = float(input("Enter the weight: "))
unit = input("Is the weight in Kilograms or Pounds? (K/L): ")
if unit == "K" or unit == "k" or unit == "Kilograms" or unit == "kilograms":
    weight = weight * 2.205
    print(f"the weight is {weight} Lbs/Pounds")
elif unit == "L" or unit == "l" or unit == "Pounds" or unit == "pounds":
    weight = weight / 2.205
    print(f"The weight is {weight} Kg/Kilograms")
else:
    print("Please enter a valid unit")
