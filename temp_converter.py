def celsius_to_fahr(temp):
    """Converts celsius temperature to Fahrenheit"""
    return 9 / 5 * temp + 32


def kelv_to_cels(temp=0):  # not necessary this defines it to make zero when not input
    """Converts kelvin temperature to celsius"""
    return temp - 273.15


def kelv_to_fahr(temp):
    """Converts kelvin temperature to Fahrenheit"""
    temp_celsius = kelv_to_cels(temp)
    temp_fahr = celsius_to_fahr(temp)
    return temp_fahr
