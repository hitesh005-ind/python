print("welcome to the in Interactive Personal Data Collector !")

name = input("please enter your name:")
age = int(input("please enter your age :"))
height = float(input("please enter your height in meters : "))
fav_num = int(input("please enter your favourite number:"))

print("\nThank you ! Here is the information we collected :\n")

print ("Name:",name)
print ("Type:",type(name))
print(" memory address:",id(name))

print("Age:",age)
print("Type:",type(age))
print(" memory address:",id(age))

print("Height:",height)
print("type:", type(height))
print(" memory address:",id(height))

print("favourite number :", (fav_num))
print("type:",type(fav_num))
print(" memory address:",id(fav_num))

birth_year=2026-age
print("\n your birth year is approximately:", birth_year)



print("Thank you for using the personal Data collector. Goodbye!")



