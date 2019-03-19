# Car rent

days = int(input('How many days?'))
kilometers = float(input('How many kilometers?'))
price = float(input('How many is the rent per day?'))
price_per_km = float(input('How many is the price per kilometer?'))

result_days = days * price

result_km = kilometers * price_per_km

total = result_days + result_km

print('Your bill is', total)
