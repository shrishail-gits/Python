n = int(input("Enter the number of days: "))

prices = []

for i in range(n):
    price = int(input("Enter the price: "))
    prices.append(price)

min_price = prices[0]
max_profit = 0

for i in range(1, n):

    if prices[i] < min_price:
        min_price = prices[i]

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit

print("Maximum profit:", max_profit)