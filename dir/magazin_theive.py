"""Видаляє записи, де amount це NaN.
Для кожного касира рахує кількість і суму повернень (groupby).
Рахує частку повернень серед усіх операцій кожного касира.
Знаходить аномалії через z-score (numpy): середнє та стандартне відхилення amount серед повернень, підозрілі ті, де z-score більший за 1.
Знаходить повернення в нічний час (після 21:00) та визначає, який касир їх робив найчастіше.
Будує два графіки в одній фігурі (matplotlib): суму повернень по касирах і кількість повернень по годинах.
Виводить висновок: ім'я підозрюваного."""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transactions = pd.DataFrame({
    "id":       range(1, 13),
    "cashier":  ["Ann", "Bob", "Cat", "Bob", "Ann", "Bob", "Cat", "Bob", "Ann", "Bob", "Cat", "Bob"],
    "type":     ["refund", "refund", "sale", "refund", "sale", "refund", "sale", "refund", "sale", "sale", "refund", "refund"],
    "amount":   [50, 200, 40, 250, 60, 300, 45, 280, 55, 70, np.nan, 320],
    "hour":     [10, 23, 11, 22, 12, 23, 13, 22, 14, 15, 16, 23],
})

#структуровка даних
transactions = transactions.dropna(subset=['amount'])
refunds = transactions[transactions["type"] == "refund"]
result = refunds.groupby("cashier")["amount"].agg(["count", "sum"])

#шукаєм частку повернень
chast = (refunds.groupby('cashier').size() / transactions.groupby('cashier').size()).fillna(0)

#виводить надпись про початок
print(f'===Перший Етап Перевірки===')
print(f'{result}\n')
print(f'---------------------------\n')

#робимо цикл в якому перебираєм всіх працівників
for cashier, chast in chast.items():
    if chast == 0:
        print(cashier, "- norm tip")
    elif chast > 0.6:
        print(f'{cashier}, {round(chast, 5)} - підозрюваний')
    else:
        print(f'{cashier}, {round(chast, 5)} - підпитанням')


#шукаємо аномалії
amounts = refunds["amount"].to_numpy()
z = (amounts - amounts.mean()) / amounts.std()
anomalies = refunds[z > 0.8]

#виводить другий етап
print(f'\n===Другий Етап Перевірки===')
print("Аномальні повернення робили:", ", ".join(anomalies["cashier"].unique())) 

#визначаємо людину яка найбільше робила повернення в нічний час
date = refunds[refunds["hour"] > 21]
date_grouped = date.groupby("cashier").size().idxmax()

#виводить третій етап
print(f'\n===Третій Етап Перевірки===')
print(f'Повернення в нічний час робив найчастіше: {date_grouped}')

#визначає топ по поверненням і аномаліям
top_refunder = refunds.groupby("cashier").size().idxmax()
top_anomaly = anomalies["cashier"].mode()[0] if not anomalies.empty else None

#визначає всиновок про підозрюваного, якщо він є
suspect = top_refunder if top_refunder == date_grouped == top_anomaly else None

#виводить підсумок
print(f'\n===Фінальний Етап Перевірки===')
print(f"Винуватець: {suspect if suspect else 'не знайдено'}")

#создаємо полотно для графіків
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

#робимо перший графік - суму повернень по касирах
color1 = ["blue", "orange", "green"]
result["sum"].plot(kind="bar", ax=axes[0], color=color1)
axes[0].set_title("Сума повернень по касирах")

#робимо другий графік - кількість повернень по годинах
color2 = ["red", "purple", "yellow"]
refunds.groupby("hour").size().plot(kind="bar", ax=axes[1], color=color2)
axes[1].set_title("Повернення по годинах")

#зжимаєм і виводимо графіки
plt.tight_layout()
plt.show()
