import sys

digit_string = sys.argv[1]
summ = 0

for digit in digit_string:
    summ += int(digit)

print(summ)
