# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_as_f = float(height)
weight_as_i = int(weight)

bmi = weight_as_i / (height_as_f ** 2)

print(int(bmi))