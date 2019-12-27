import math
f = open('input.txt')

modules = f.readlines()
total_fuel = 0

def calculateFuelReq(mass, cumulative_fuel = 0):
    fuel_part = math.floor(int(mass) / 3) - 2

    if fuel_part >= 0:
        return calculateFuelReq(fuel_part, cumulative_fuel + fuel_part)
    else:
        return cumulative_fuel


for module_mass in modules:
    total_fuel += calculateFuelReq(module_mass.strip())

print("Total fuel requirement:" + str(total_fuel))

# SOLUTION: 5046772