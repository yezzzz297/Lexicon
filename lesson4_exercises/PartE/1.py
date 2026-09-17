
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def classify_temperature(temp_c):
    if temp_c < 10:
        return "cold"
    if temp_c < 25:
        return "warm"
    return "hot"


def format_report(city, celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    feeling = classify_temperature(celsius)
    return f"{city}: {celsius}C ({fahrenheit}F) - {feeling}"


print(format_report("London", 30))
print(format_report("Sweden", 8))
