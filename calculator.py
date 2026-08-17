from config import VOLTAGE_MIN, VOLTAGE_MAX, VOLTAGE_STEP
import numpy as np


def get_voltages():
    voltages = list(range(VOLTAGE_MIN, VOLTAGE_MAX + 1, VOLTAGE_STEP))
    return np.array(voltages)

def numpy_Series_calculation():
	print("write resistances like 1,2,3,4,5")
	resistances = input("Series of: ")	
	series_resistances = np.array([int(r) for r in resistances.split(",")])
	total_resistance = np.sum(series_resistances)
	return total_resistance

def numpy_Parallel_calculation():
	print("write resistances like 1,2,3,4,5")
	resistances = input("Parallel of: ")
	parallel_resistances = np.array([int(r) for r in resistances.split(",")])
	total_resistance = 1 / np.sum(1 / parallel_resistances)
	return total_resistance

def get_resistance():
    while True:
        try:
            resistance = float(input("Enter the resistance value (in ohms): "))
            if resistance <= 0:
                print("Resistance must be a positive value. Please try again.")
                continue
            return resistance
        except ValueError:
            print("Invalid input. Please enter a numeric value for resistance.")

def Series_calculation():
    resistance = []
    while True:
        try:
            resistance.append(get_resistance())
        except ValueError:
            print("Invalid input. Please enter a numeric value for resistance.")
            continue
        more = input("Do you want to add another resistor in series? (y/n): ")
        if more.lower() != 'y':
            break
    total_resistance = sum(resistance)
    return total_resistance

def Parallel_calculation():
    resistance = []
    while True:
        try:
            resistance.append(get_resistance())
        except ValueError:
            print("Invalid input. Please enter a numeric value for resistance.")
            continue
        more = input("Do you want to add another resistor in parallel? (y/n): ")
        if more.lower() != 'y':
            break
    total_resistance = 1 / sum(1 / r for r in resistance)
    return total_resistance