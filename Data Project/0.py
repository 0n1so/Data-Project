import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import random


print("\n=== ПЕРЕВІРКА УСПІШНОСТІ === \n")

start_time = time.time()

product = np.array(['electronic', 'clothes', 'shoes', 'book', 'makeup'])
records = []

for _ in range(200):
    product_item = random.choice(product)
    count = random.randint(1, 50)
    price = random.randint(50, 5000)
    sum_sell = count * price
    records.append({"Product": product_item, "Revenue": sum_sell})

df = pd.DataFrame(records)
print(df)

grouped = df.groupby("Product")["Revenue"].sum()

best_category = grouped.idxmax()
best_revenue = grouped.max()
average_revenue = np.mean(grouped.values)
std_revenue = np.std(grouped.values)
general_sum = grouped.sum()


colors = ["#2d166d", "#b12230", "#4aaa31", "#cf9f37", "#b21cb8"]

plt.bar(grouped.index, grouped.values, color=colors)
plt.ticklabel_format(style='plain', axis='y')
plt.ylabel("Сума виручки")
plt.xlabel("Продукт")
plt.title("Загальна виручка по категоріях")

end_time = time.time()
total_time = end_time - start_time


print(f" -------Статистика--------\n"
      f" Категорія з найбільшою виручкою: {best_category} ({best_revenue})\n"
      f" Середня виручка: {round(average_revenue, 2)}\n"
      f" Середнє відхилення: {round(std_revenue, 2)}\n\n"
      f" Загальна виручка магазину: {general_sum}\n\n"
      f" Часу затрачено на статистику: {round(total_time, 7)}")

if general_sum < 500_000:
    print(f"\n УВАГА: виручка низька — {general_sum} грн. Місяць невдалий.")
else:
    print(f"\n Місяць успішний! Загальна виручка: {general_sum} грн")

plt.show()

os.system("cls" if os.name == "nt" else "clear")
print("\033[H\033[J", end="")

print("Terminal is clear")