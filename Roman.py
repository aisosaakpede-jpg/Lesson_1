# Take the roman numeral from the user and change it to an integer

num = int(input("Enter number between 1 and 3999"))

values = [1000, 900, 500, 400, 100,
           50, 40, 10, 9, 5, 4, 1]

symbols = ["M","CM", "D", "CD", "C", "L",
            "XL", "X", "IX", "V", "IV","I"]


roman = ""

for i in range(len(values)):
    while num >= values[i]:
        roman = roman + symbols[i]
        num = num - values[i]

print("Roman numerals: ",roman) 