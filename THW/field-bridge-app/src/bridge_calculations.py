def calculate_load(span, load_per_unit_length):
    """
    Calculate the total load on the bridge based on the span and load per unit length.
    
    Parameters:
    span (float): The span of the bridge in meters.
    load_per_unit_length (float): The load per unit length in kg/m.
    
    Returns:
    float: The total load in kg.
    """
    return span * load_per_unit_length

def calculate_span(length, width):
    """
    Calculate the span of the bridge based on the length and width of the field.
    
    Parameters:
    length (float): The length of the field in meters.
    width (float): The width of the field in meters.
    
    Returns:
    float: The span of the bridge in meters.
    """
    return length + width  # Simplified calculation for demonstration

def calculate_bridge_parameters(length, width, load_per_unit_length):
    """
    Calculate various parameters for the bridge design.
    
    Parameters:
    length (float): The length of the field in meters.
    width (float): The width of the field in meters.
    load_per_unit_length (float): The load per unit length in kg/m.
    
    Returns:
    dict: A dictionary containing the span and total load.
    """
    span = calculate_span(length, width)
    total_load = calculate_load(span, load_per_unit_length)
    
    return {
        'span': span,
        'total_load': total_load
    }