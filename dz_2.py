"""
Определите среднюю зарплату (Salary) по городу (City)
- используйте файл приложенный к дз - dz.csv
"""
import pandas as pd

df = pd.read_csv('dz.csv')
# print(df.info())

# группировка и расчет в группе
group = df.groupby('City')['Salary'].mean()
print('Средняя зарплата по городу')
print(group)
