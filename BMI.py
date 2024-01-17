# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters e.g., 1.55: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72: "))


#BMI Calculator and its logic

Bmi = weight / (height*height)
if  Bmi < 18.5 :
  print("\nYour BMI is "+ str(Bmi) + ", you are underweight.")
elif  Bmi > 18.5 and Bmi < 25:
  print("\nYour BMI is "+str(Bmi)+", you have a normal weight.")
elif   Bmi >= 25 and Bmi < 30:
  print("\nYour BMI is "+str(Bmi)+", you are slightly overweight.")
elif  Bmi >= 30 and Bmi < 35:
  print("\nYour BMI is "+str(Bmi)+", you are obese.")
elif  Bmi >= 35:
  print("\nYour BMI is "+str(Bmi)+", you are clinically obese.")