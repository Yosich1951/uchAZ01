"""
World-happiness-report-2024.csv
"""
import pandas as pd
df = pd.read_csv('World-happiness-report-2024.csv')
# первые
print(df.head())
# последние
print(df.tail())
# базовая информацмя
print(df.info())
# статистика
print(df.describe())
# столбец
print(df['Country name'])
# столбцы
print(df[['Country name', 'Regional indicator']])
# строка
print(df.loc[56])
# строка и столбец
print(df.loc[56, 'Healthy life expectancy'])
# по условию
print(df[df['Healthy life expectancy'] > 0.7])





