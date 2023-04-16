import json

with open("file.txt", "r") as f:
    lines = f.readlines()

profits = {}
total_profit = 0
count_profit = 0

for line in lines:
    company, revenue, expenses = line.split()
    profit = int(revenue) - int(expenses)
    if profit > 0:
        profits[company] = profit
        total_profit += profit
        count_profit += 1

average_profit = total_profit / count_profit
result = [profits, {"average_profit": average_profit}]

with open("result.json", "w") as f:
    json.dump(result, f)