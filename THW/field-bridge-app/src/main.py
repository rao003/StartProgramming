# main.py

from measurements import get_field_dimensions
from bridge_calculations import calculate_bridge_parameters

def main():
    # Get field dimensions
    length, width = get_field_dimensions()
    
    # Calculate bridge parameters
    load, span = calculate_bridge_parameters(length, width)
    
    # Output results
    print(f"Field Length: {length} meters")
    print(f"Field Width: {width} meters")
    print(f"Calculated Load: {load} kg")
    print(f"Calculated Span: {span} meters")

if __name__ == "__main__":
    main()