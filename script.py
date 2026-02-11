import pandas as pd

file_path = 'data_student.csv'


df = pd.read_csv(file_path)
print(f"{df}")