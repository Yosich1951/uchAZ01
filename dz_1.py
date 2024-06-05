"""
Скачайте любой датасет с сайта https://www.kaggle.com/datasets
Загрузите набор данных из CSV-файла в DataFrame.
Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
Выведите информацию о данных (.info()) и статистическое описание (.describe()).
"""

import pandas as pd

df = pd.read_csv('Thyroid_Diff.csv')

# Выведите первые 5 строк данных
print(df.head())

# Выведите информацию о данных (.info())
print(df.info())

# Выведите статистическое описание (.describe())
print(df.describe())

