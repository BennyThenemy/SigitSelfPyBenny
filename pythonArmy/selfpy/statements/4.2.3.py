temperature = input("Insert the temperature you would like to convert: ")
letter = temperature[-1].upper()
temperature = temperature[:-1]

if letter == 'C':
    temperature_F = (int(temperature) * 9/5) + 32
    print(f"Celsius - > Fahrenheit: {temperature_F}")

elif letter == 'F':
    temperature_C = (int(temperature) - 32) * 5/9
    print(f"Fahrenheit - > Celsius: {temperature_C}")

else:
    print("Missing data")
