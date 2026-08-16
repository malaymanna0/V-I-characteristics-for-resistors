import sys
from calculator import Series_calculation, Parallel_calculation, get_voltages
from plotter import plot_vi_curves

def main():
    print("Welcome to the V-I Characteristics Calculator!")
    print("Choose the type of resistor configuration:")
    print("1. Series")
    print("2. Parallel")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        resistance = Series_calculation()
    elif choice == '2':
        resistance = Parallel_calculation()
    else:
        sys.exit("Invalid choice. Please run the program again and select either 1 or 2.")
        
    
    voltages = get_voltages()
    currents = voltages / resistance  # Ohm's Law: I = V / R
    plot_vi_curves(voltages, currents, resistance)

if __name__ == "__main__":
    main()