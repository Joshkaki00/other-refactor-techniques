# by Kami Bigdely 
COULOMBS_CONSTANT = 8.9875517923 * 1e9  # N·m²/C²
EVEN_DIVISOR = 2

# Given two point charges, calcualte the electric force exerted on them.
def calculate_electric_force(q1, q2, distance):
    return COULOMBS_CONSTANT * q1 * q2 / (distance ** 2)


q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = COULOMBS_CONSTANT * q1 * q2 / (distance ** 2)
print("Electric Force between q1 and q2 is: ", force, "Newton")
# Second Section
num = int(input('Enter an integer number: '))
if num % EVEN_DIVISOR == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")