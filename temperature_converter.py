# Temperature converter


celsius = float(input('What temperature in Celsius?'))

fahrenheit = float(input('What temperature in Fahrenheit?'))

result_celsius_to_fahrenheit = ((9*celsius)/5)+32

print('Celsius to Fahrenheit: ', result_celsius_to_fahrenheit)

result_fahrenheit_to_celsius = (fahrenheit - 32)*5/9

print('Fahrenheit to Celsius: ', result_fahrenheit_to_celsius)