import os
import pandas as pd
from catboost.datasets import titanic


DATASETS_PATH = "../datasets"

if not os.path.exists(DATASETS_PATH):
    try:
        os.makedirs(DATASETS_PATH)
        print(f"The {DATASETS_PATH} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")


train_df = titanic()
print(train_df.info())

# Сохранение датасета в CSV
try:
    train_df.to_csv('../datasets/dataset_titanic.csv', index=False)
    print("Datasets successfully saved in the directory ../dataset under names dataset_titanic.csv.")
except Exception as e:
    print("Error:", e)