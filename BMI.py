# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters e.g., 1.55: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72: "))


#BMI Calculator and its logic
Bmi = weight / (height*height)
if  Bmi < 18.5 :
  print(f"Your BMI is {Bmi}, you are underweight.")
elif  Bmi  < 25:
  print(f"Your BMI is {Bmi}, you have a normal weight.")
elif   Bmi < 30:
  print(f"Your BMI is {Bmi}, you are slightly overweight.")
elif  Bmi < 35:
  print(f"Your BMI is {Bmi}, you are obese.")
else:
  print(f"Your BMI is {Bmi}, you are clinically obese.")
  
