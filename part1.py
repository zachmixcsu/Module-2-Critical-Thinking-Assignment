bill_price = float(input('whats the price of the bill?: '))

tip = bill_price * 0.18

tax = bill_price * 0.07

print(f'Tip: {round(tip,2)}')
print(f'Tax: {round(tax,2)}')
print(f'Total: {round(bill_price + tip + tax,2)}')