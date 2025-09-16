# d_bruecke_data.py

# This file contains the data related to the D-brücke configurations, including a lookup table with various configurations, maximum spans, and load capacities.

D_BRUECKE_CONFIGURATIONS = {
    'Standard': [
        (10.0, 20),  # Example: Standard configuration can support a load of 20 tons up to 10.0m
        (15.0, 15),
        (20.0, 10),
    ],
    'Heavy-Duty': [
        (12.0, 30),
        (18.0, 25),
        (24.0, 20),
    ],
    'Lightweight': [
        (8.0, 10),
        (12.0, 5),
    ],
    'Extended': [
        (15.0, 40),
        (20.0, 35),
        (30.0, 30),
    ],
    'Custom': [
        (25.0, 50),
        (30.0, 45),
    ]
}