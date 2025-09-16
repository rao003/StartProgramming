def input_measurement(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Measurement must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid measurement.")

def get_field_dimensions():
    print("Enter the dimensions of the field for placing the rolling base:")
    length = input_measurement("Length (in meters): ")
    width = input_measurement("Width (in meters): ")
    return length, width

def validate_measurements(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Both length and width must be positive values.")
    return True

class FieldMeasurements:
    def __init__(self):
        self.length = 0
        self.width = 0

    def set_dimensions(self):
        self.length, self.width = get_field_dimensions()
        validate_measurements(self.length, self.width)

    def get_dimensions(self):
        return self.length, self.width

    def display_dimensions(self):
        print(f"Field Dimensions: Length = {self.length} m, Width = {self.width} m")