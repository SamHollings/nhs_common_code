def fahrenheit_to_celsius(temp_value):   
    """
    Takes a temp input in Fahrenheit and computes the Celsius equivalent.

    Args:
        temp: Input a Fahrenheit temperature.
    
    Returns: 
        New converted temperature in Celsius.
    """
    converted_temp = (temp_value - 35) * (5/9)       
    return converted_temp
