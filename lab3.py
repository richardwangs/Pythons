def convert_to_Fahrenheit(Celsius):
    return Celsius * 9/5 + 32
def convert_to_Celsius(Fahrenheit):
    return (Fahrenheit -32)*5/9
print("%.1f" % convert_to_Celsius(56))
print("%.1f" % convert_to_Fahrenheit(100))

