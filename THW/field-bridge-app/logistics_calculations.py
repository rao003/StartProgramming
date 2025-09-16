# logistics_calculations.py

# A simplified model for logistics calculations.
# These calculations assume a flat approach and a standard launching nose.
# A full engineering analysis would require more complex variables
# such as terrain profile and wind load.

def calculate_roller_placement(bridge_span_m, num_panels):
    """
    Calculates the ideal placement of the rocking roller base.
    The formula is a simplified model based on maintaining a stable cantilever
    during the bridge launch. It accounts for the length of the launching nose.

    Args:
        bridge_span_m (float): The gap the bridge needs to span.
        num_panels (int): The number of panels per chord in the main bridge structure.

    Returns:
        float: The distance from the edge of the near bank to the center of the roller base.
    """
    # Each panel is 3.048m (10 feet). A standard launching nose is often 4 panels long.
    LAUNCHING_NOSE_PANELS = 4
    PANEL_LENGTH_M = 3.048

    # The total length of the structure being launched
    total_launch_length = (num_panels + LAUNCHING_NOSE_PANELS) * PANEL_LENGTH_M

    # Simplified rule for roller placement: The roller should be placed such that the
    # center of gravity of the cantilevered portion is just over the rollers
    # at the point of maximum overhang.
    # A good rule of thumb is to place the rollers at a distance from the
    # near bank equal to 1.5 times the length of a panel. This provides a
    # stable pivot point as the bridge is launched.
    roller_distance_from_bank = 1.5 * PANEL_LENGTH_M

    print(f"\n--- Roller Placement Calculation ---")
    print(f"Total panels being launched (including nose): {num_panels + LAUNCHING_NOSE_PANELS}")
    print(f"Total launch length: {total_launch_length:.2f} meters")
    print(f"Recommended roller placement from bank edge: {roller_distance_from_bank:.2f} meters")
    return roller_distance_from_bank


def calculate_height_adjustment(near_bank_elevation_m, far_bank_elevation_m, bridge_span_m):
    """
    Calculates the required vertical height adjustment to ensure the bridge lands correctly.
    This compensates for both the elevation difference between banks and the natural sag (deflection) of the bridge.

    Args:
        near_bank_elevation_m (float): The elevation of the near bank where launching begins.
        far_bank_elevation_m (float): The elevation of the far bank where the bridge will land.
        bridge_span_m (float): The length of the gap the bridge needs to span.

    Returns:
        float: The height (in meters) to raise or lower the near-bank roller base.
    """
    # A standard Bailey bridge will have a natural sag (deflection) under its own weight
    # and this needs to be pre-compensated. The sag is typically a small percentage of the span.
    # We'll use a rule of thumb: Sag is approx. 1/400th of the span.
    # This is a general approximation and should be verified with a structural engineer.
    sag_compensation_m = bridge_span_m / 400

    # Calculate the elevation difference between the two banks
    elevation_difference_m = far_bank_elevation_m - near_bank_elevation_m

    # The total adjustment needed is the sum of the elevation difference and the sag compensation.
    # A positive value means the near bank needs to be higher.
    required_adjustment_m = elevation_difference_m + sag_compensation_m

    print(f"\n--- Height Adjustment Calculation ---")
    print(f"Elevation difference (far - near): {elevation_difference_m:.2f} meters")
    print(f"Calculated sag compensation: {sag_compensation_m:.2f} meters")
    print(f"Required height adjustment: {required_adjustment_m:.2f} meters")

    return required_adjustment_m


# Example Usage:
# Assume a 20.0m span, 12 panels, near bank at 100m, far bank at 101.5m
# span = 20.0
# panels = 12
# near_elev = 100.0
# far_elev = 101.5

# roller_position = calculate_roller_placement(span, panels)
# height_adjust = calculate_height_adjustment(near_elev, far_elev, span)

# if roller_position and height_adjust:
#     print(f"\nFinal Recommendations:")
#     print(f"Place the rocking roller base {roller_position:.2f}m from the bank edge.")
#     if height_adjust > 0:
#         print(f"Raise the roller base by {height_adjust:.2f}m.")
#     else:
#         print(f"Lower the roller base by {-height_adjust:.2f}m.")
# else:
#     print("Calculations failed. Please check your inputs.")