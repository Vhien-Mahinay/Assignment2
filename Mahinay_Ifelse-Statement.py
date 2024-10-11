#Input grades for 5 different subjects
Math = float(input("Enter Grade for Math:"))
English = float(input("Enter Grade for English:"))
Science = float(input("Enter Grade for Science:"))
PE = float(input("Enter Grade For PE:"))
Arts = float(input("Enter Grade for Arts:"))

#Calculating for average grade
Average = (Math + English + Science + PE + Arts) / 5

#Display average grade
print(f"Your Average Grade is: {Average:.2f}")

#Checking if passed or failed
if Average >= 75:
    print("Passed")
else:
    print("Failed")



