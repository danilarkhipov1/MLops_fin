import os
from catboost.datasets import titanic
from collections import Counter


DATASETS_PATH = "../datasets/"

if not os.path.exists(DATASETS_PATH):
    try:
        os.makedirs(DATASETS_PATH)
        print(f"The {DATASETS_PATH} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")


train_df = titanic()

# Заполнение пропущенных значений на max значения
train_df['Age'] = 0


# Подсчитываем количество встречаемости каждого значения в столбце 'Embarked'
counter = Counter(train_df['Embarked'])
least_common_value = counter.most_common()[-1][0]  # Находим наименее встречаемое значение

# Заменяем значения на наименее встречаемое значение
train_df['Embarked'] = train_df['Embarked'].fillna(0)

# Сохранение датасета в CSV
try:
    train_df.to_csv('../datasets/dataset_titanic.csv', index=False)
    print("MODIFIED dataset successfully saved in the directory ../dataset under names dataset_titanic.csv.")
except Exception as e:
    print("An error occurred while saving datasets:", e)