#Function to Convert Temperature

def convert_temperature(celsius=None, fahrenheit=None):
    if celsius is not None:
        return (celsius * 9/5) + 32
    elif fahrenheit is not None:
        return (fahrenheit - 32) * 5/9
