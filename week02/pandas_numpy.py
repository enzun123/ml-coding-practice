import pandas as pd

file_url='https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample.csv'
sample=pd.read_csv(file_url)

print(sample.head())
print(sample.tail())

sample.info()
sample.describe()

sample_dic={'name':['join','Ann','Kevin'], 'age':[23,22,21]}
a = pd.DataFrame(sample_dic)

a.info()

pd.DataFrame