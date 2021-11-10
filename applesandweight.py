one_apple_weight_kg = 0.2
one_apple_pounds_kg = 0.440925
amount_apples = int(input("How many apples do you have? "))
weight_selection = input("Is that in Kilos (kg) or Pounds (lbs)? ").upper()
# print(amount_apples)
# print(weight_selection)

if weight_selection == "KG":
    kg_amount = amount_apples * one_apple_weight_kg
    print("Your apples in KG is " + str(kg_amount))

if weight_selection == "LBS":
    lbs_amount = amount_apples * one_apple_pounds_kg
    print("Your apples in LBS is " + str(lbs_amount))

