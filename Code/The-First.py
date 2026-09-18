import os 
import random


def profit_margin(revenue, cost):
    if revenue == 0:
        return 0
    profit = revenue - cost
    margin = (profit / revenue) * 100
    return round(margin, 2)

result = profit_margin(2, 1.98)
print(result)

x = profit_margin

random_x = random.randint(1, 3)
if random_x == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
else: 
    if random_x != 1:
        print("all is okey")
        
