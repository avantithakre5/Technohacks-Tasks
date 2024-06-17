def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def get_temperature_input(scale):
    """Get a temperature value from the user, with validation."""
    while True:
        try:
            temp = float(input(f"Enter the temperature in {scale}: "))
            return temp
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_conversion_choice():
    """Get the user's choice of conversion, with validation."""
    while True:
        print("\nChoose the conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = input("Enter the number of your choice: ")
        if choice in ['1', '2']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    """Main function to perform temperature conversions based on user input."""
    while True:
        choice = get_conversion_choice()
        if choice == 1:
            celsius = get_temperature_input("Celsius")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        elif choice == 2:
            fahrenheit = get_temperature_input("Fahrenheit")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        
        again = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the temperature converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
