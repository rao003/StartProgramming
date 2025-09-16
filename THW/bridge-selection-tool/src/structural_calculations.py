# filepath: /bridge-selection-tool/bridge-selection-tool/src/structural_calculations.py

BRIDGE_CONFIGURATIONS = {
    'Single-Single': [
        (12.2, 70),
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
    if span_m <= 0 or load_class_tons <= 0:
        return None, None, None

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
            if span_m <= max_span and load_class_tons <= max_load:
                num_panels = int(span_m / 3.048)
                if span_m % 3.048 != 0:
                    num_panels += 1

                num_panels = max(num_panels, 4)

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
                
                total_panels = num_panels * wall_multiplier * story_multiplier
                total_transoms = num_panels + 1
                
                components = {
                    "Panel": total_panels,
                    "Transom": total_transoms,
                    "Panel Pin": total_panels * 2,
                    "Male End Post": story_multiplier,
                    "Female End Post": story_multiplier,
                }
                
                return config, num_panels, components

    return None, None, None