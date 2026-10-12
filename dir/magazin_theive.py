"""Видаляє записи, де amount це NaN.
Для кожного касира рахує кількість і суму повернень (groupby).
Рахує частку повернень серед усіх операцій кожного касира.
Знаходить аномалії через z-score (numpy): середнє та стандартне відхилення amount серед повернень, підозрілі ті, де z-score більший за 1.
Знаходить повернення в нічний час (після 21:00) та визначає, який касир їх робив найчастіше.
Будує два графіки в одній фігурі (matplotlib): суму повернень по касирах і кількість повернень по годинах.
Виводить висновок: ім'я підозрюваного."""

#імпортуєм бібліотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#создаєм масив даних про транзакції
transactions = pd.DataFrame({
    "id":       range(1, 13),
    "cashier":  ["Ann", "Bob", "Cat", "Bob", "Ann", "Bob", "Cat", "Bob", "Ann", "Bob", "Cat", "Bob"],
    "type":     ["refund", "refund", "sale", "refund", "sale", "refund", "sale", "refund", "sale", "sale", "refund", "refund"],
    "amount":   [50, 200, 40, 250, 60, 300, 45, 280, 55, 70, np.nan, 320],
    "hour":     [10, 23, 11, 22, 12, 23, 13, 22, 14, 15, 16, 23],
})

#структуровка даних -> видаляєм записи з NaN
transactions = transactions.dropna(subset=['amount'])
#шукаєм повернення і групуєм по касирам
refunds = transactions[transactions["type"] == "refund"]
#рахуєм кількість і суму повернень по касирам
result = refunds.groupby("cashier")["amount"].agg(["count", "sum"])

#шукаєм частку повернень -> ділим кількість повернень на кількість всіх операцій по касирам + fillna(0) для заповнення NaN нулями
chast = (refunds.groupby('cashier').size() / transactions.groupby('cashier').size()).fillna(0)

#виводить надпись про початок
print(f'===Перший Етап Перевірки===')
print(f'{result}\n')
print(f'---------------------------\n')

#робимо цикл в якому перебираєм всіх працівників -> берем імя касирів і приміряєм частку повернень
#якщо частка 0 - норм, якщо більше 0.6 - підозрюваний, інакше підпитанням
for cashier, chast in chast.items():
    if chast == 0:
        print(cashier, "- norm tip")
    elif chast > 0.6:
        print(f'{cashier}, {round(chast, 5)} - підозрюваний')
    else:
        print(f'{cashier}, {round(chast, 5)} - підпитанням')


#шукаємо аномалії -> переводим таблицю в numpy
amounts = refunds["amount"].to_numpy()
#рахуєм z-score і відбираєм аномалії де z-score > 0.8 (z = (сума - mean) / std)
z = (amounts - amounts.mean()) / amounts.std()
anomalies = refunds[z > 0.8]

#виводить другий етап
print(f'\n===Другий Етап Перевірки===')
print("Аномальні повернення робили:", ", ".join(anomalies["cashier"].unique())) 

#визначаємо людину яка найбільше робила повернення в нічний час
date = refunds[refunds["hour"] > 21]
#сайз рахує кількість повернень по касирам, idxmax() повертає імя касира з найбільшою кількістю повернень в нічний час
date_grouped = date.groupby("cashier").size().idxmax()

#виводить третій етап
print(f'\n===Третій Етап Перевірки===')
print(f'Повернення в нічний час робив найчастіше: {date_grouped}')

#висновок через систему балів
#рахуєм частку повернень по касирам і зберігаєм в змінну share, fillna(0) щоб заповнити NaN нулями
share = (refunds.groupby("cashier").size() / transactions.groupby("cashier").size()).fillna(0)
#рахуєм кількість повернень в нічний час по касирам і зберігаєм в змінну night, reindex(share.index, fill_value=0) щоб додати всіх касирів навіть якщо вони не робили нічних повернень
night = refunds[refunds["hour"] > 21].groupby("cashier").size().reindex(share.index, fill_value=0)


#создаєм фрейм з індексом касирів 
flags = pd.DataFrame(index=share.index)
#дізнаємся чи частка повернень > 0.6
flags["high_chast"] = share > 0.6
#дізнаємся чи робив касир аномальні повернення
flags["anomaly"] = flags.index.isin(anomalies["cashier"])
#дізнаємся чи робив касир повернення в нічний час >= 2
flags["night"] = night >= 2
#рахуєм суму балів по кожному касиру
flags["score"] = flags.sum(axis=1)

#визначаємо винних - ті у кого score >= 2
guilty = flags[flags["score"] >= 2].index.tolist()

#виводить підсумок
print(f'\n===Фінальний Етап Перевірки===')
print(flags)
print(f"Винні: {', '.join(guilty) if guilty else 'не знайдено'}")

#робить графіки на чорному фоні
plt.style.use("dark_background")

#визначаємо середнє значення суми повернень
mean = refunds["amount"].mean()

#создаєм один раз фігуру і додаєм два графіки в один рядок
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

#перший графік - повернення, ніч і середнє
#будуєм перший графік по годинам і сумрю повернень, додаєм легенду і колір
axes[0].scatter(refunds["hour"], refunds["amount"], color="cyan", label="повернення")
#додаєм червоний прямокутник на графік для позначення нічного часу (21-24 години) + додаєм легенду, прозорість, колір
axes[0].axvspan(21, 24, color="red", alpha=0.25, label="ніч")
#виводим середнє значення на графік як пунктирну лінію і надаєм їй оранжевий колір і легенду
axes[0].axhline(mean, color="orange", linestyle="--", label="середнє")
#робим анотацію щоб показати макс точку на графіку, xy - координати точки, xytext - координати тексту, arrowprops - властивості стрілки
axes[0].annotate("max", xy=(23, 320), xytext=(15, 300),
                 arrowprops=dict(arrowstyle="->", color="white"))
#додаєм заголовок, підписи осей і легенду
axes[0].set_title("Повернення і середнє")
axes[0].set_xlabel("година")
axes[0].set_ylabel("сума")
axes[0].legend()

#другий графік - кількість повернень по годинах
#робим групування по годинах і рахуєм кількість повернень, будуєм графік типу bar, додаєм колір і ставим його справа від першого графіка
refunds.groupby("hour").size().plot(kind="bar", ax=axes[1], color="cyan")
#додаєм заголовок, підписи осей
axes[1].set_title("Повернення по годинах")
axes[1].set_xlabel("година")
axes[1].set_ylabel("кількість")

#зжимаєм і виводимо графіки
plt.tight_layout()
plt.show()