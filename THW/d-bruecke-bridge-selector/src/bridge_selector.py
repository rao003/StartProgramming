def get_bridge_configuration(span_m, load_class_tons):
    D_BRUECKE_CONFIGURATIONS = {
        'Type A': [
            (10.0, 20),
            (15.0, 15),
            (20.0, 10),
        ],
        'Type B': [
            (12.0, 25),
            (18.0, 20),
            (24.0, 15),
        ],
        'Type C': [
            (15.0, 30),
            (20.0, 25),
            (30.0, 20),
        ],
        'Type D': [
            (20.0, 40),
            (25.0, 30),
            (30.0, 25),
        ],
    }

    if span_m <= 0 or load_class_tons <= 0:
        return None, None, None

    for config, specs in D_BRUECKE_CONFIGURATIONS.items():
        for max_span, max_load in specs:
            if span_m <= max_span and load_class_tons <= max_load:
                return config, max_span, max_load

    return None, None, None

def main():
    print("Welcome to the D-Brücke Bridge Selector!")
    try:
        span_m = float(input("Enter the required span of the bridge in meters: "))
        load_class_tons = int(input("Enter the required load capacity in tons: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    config, max_span, max_load = get_bridge_configuration(span_m, load_class_tons)

    if config:
        print(f"Recommended Bridge Configuration: {config}")
        print(f"Maximum Span: {max_span}m, Maximum Load: {max_load} tons")
    else:
        print("No valid bridge configuration found for the given requirements.")

if __name__ == "__main__":
    main()