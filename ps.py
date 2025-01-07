roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
roman = "MCMXCIV"
total = 0
for i in range(len(roman)):
    if i + 1 < len(roman) and roman_values[roman[i]] < roman_values[roman[i + 1]]:
        total -= roman_values[roman[i]]
    else:
        total += roman_values[roman[i]]
print("Integer value:",total)