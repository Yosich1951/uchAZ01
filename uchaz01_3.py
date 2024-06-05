"""
3. Функции редактирования и анализа датафрейма
"""

import pandas as pd

# # считать данные
# df = pd.read_csv('hh.csv')
# # добавить столбец
# df['Test'] = [new for new in range(29)]
# print(df)
# # удалить столбец в исходном фрейме
# df.drop('Test', axis=1, inplace=True)
# print(df)
# # удалить строку в исходном фрейме
# df.drop(28, axis=0, inplace=True)
# print(df)

# Редактирование и удаление данных
# считать данные
df2 = pd.read_csv('animal.csv')
print(df2)
# заполнить недостающие данные значением 0
df2.fillna(0, inplace=True)
print(df2)
# удаление не рекомендуется
# df.dropna(inplace=True)
# группировка и расчет в группе
group = df2.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

# сохранить изменения в другом файле без индекса
# df2.to_csv('animal_out.csv', index=False)