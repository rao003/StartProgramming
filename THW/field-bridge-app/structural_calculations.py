# structural_calculations.py

# A simplified lookup table based on standard Bailey bridge manuals.
# The values are approximate and should be verified with official
# engineering documentation for a real-world application.
# Format: {'Configuration': [(max_span_m, load_class_tons), ...]}
# Load classes are based on standard military designations (e.g., Class 40, Class 70).

BRIDGE_CONFIGURATIONS = {
    'Single-Single': [
        (12.2, 70),  # Example: Single-Single can support a Class 70 load up to 12.2m
        (18.3, 40),
        (24.4, 12),
    ],
    'Single-Double': [
        (18.3, 70),
        (24.4, 40),
        (30.5, 12),
    ],
    'Single-Triple': [
        (24.4, 70),
        (30.5, 40),
        (36.6, 12),
    ],
    'Double-Single': [
        (24.4, 70),
        (30.5, 40),
        (42.7, 12),
    ],
    'Double-Double': [
        (30.5, 70),
        (36.6, 40),
        (48.8, 12),
    ],
    'Double-Triple': [
        (36.6, 70),
        (42.7, 40),
        (54.9, 12),
    ]
}

def calculate_bridge_configuration(span_m, load_class_tons):
    """
    Calculates the required bridge configuration (single, double, triple, single/double story)
    based on the span and load class.

    Args:
        span_m (float): The required span of the bridge in meters.
        load_class_tons (int): The required load capacity in tons.

    Returns:
        tuple: A tuple containing (configuration_name, num_panels, components_list)
               or (None, None, None) if no valid configuration is found.
    """
    if span_m <= 0 or load_class_tons <= 0:
        return None, None, None

    # Sort configurations by complexity to find the simplest valid one first
    sorted_configs = sorted(
        BRIDGE_CONFIGURATIONS.keys(),
        key=lambda k: (
            k.count('Single'),
            k.count('Double'),
            k.count('Triple')
        )
    )

    for config in sorted_configs:
        for max_span, max_load in BRIDGE_CONFIGURATIONS[config]:
            # Check if this configuration is sufficient
            if span_m <= max_span and load_class_tons <= max_load:
                # Calculate the number of panels needed. Each panel is 3.048m long.
                num_panels = int(span_m / 3.048)
                if span_m % 3.048 != 0:
                    num_panels += 1

                # Ensure minimum panels for stability
                num_panels = max(num_panels, 4)

                # Now, calculate the number of components based on the configuration and panels.
                # This is a simplified calculation and will be refined later.
                wall_multiplier = 1
                story_multiplier = 1
                
                if 'Single' in config:
                    wall_multiplier = config.count('Single')
                elif 'Double' in config:
                    wall_multiplier = config.count('Double') * 2
                elif 'Triple' in config:
                    wall_multiplier = config.count('Triple') * 3

                if config.startswith('Double'):
                    story_multiplier = 2
                
                # We need to account for panels in each story and wall
                total_panels = num_panels * wall_multiplier * story_multiplier
                total_transoms = num_panels + 1 # One transom at each panel junction and one at each end
                
                # A full component list will be generated in the next step
                # For now, we'll return a simplified list
                components = {
                    "Panel": total_panels,
                    "Transom": total_transoms,
                    "Panel Pin": total_panels * 2, # Two pins per panel connection
                    "Male End Post": story_multiplier,
                    "Female End Post": story_multiplier,
                }
                
                return config, num_panels, components

    # If no configuration is found
    return None, None, None

# Example usage:
# required_span = 20.0
# required_load = 40
# config, num_panels, components = calculate_bridge_configuration(required_span, required_load)

# if config:
#     print(f"Required Span: {required_span}m, Required Load: {required_load} tons")
#     print(f"Recommended Configuration: {config}")
#     print(f"Number of Panels per Chord: {num_panels}")
#     print("Estimated Component List:")
#     for item, count in components.items():
#         print(f"  - {item}: {count}")
# else:
#     print(f"No valid configuration found for a span of {required_span}m and load of {required_load} tons.")