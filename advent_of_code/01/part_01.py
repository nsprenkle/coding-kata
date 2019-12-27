import math
f = open('input.txt')

modules = f.readlines()
total_fuel = 0

def calculateFuelReq(mass):
    return math.floor(int(mass) / 3) - 2


for module_mass in modules:
    total_fuel += calculateFuelReq(module_mass.strip())

print("Total fuel requirement:" + str(total_fuel))

# SOLUTION: 3366415