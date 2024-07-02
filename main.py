import pandas as pd

data = {
    'Name': ['Игорь', 'Олег', 'Андрей', 'Карина', 'Олеся', 'Тарас', 'Оксана', 'Арсен', 'Роберт', 'Камилла'],
    'Mathematics': [9, 8, 9, 7, 6, 8, 9, 8, 9, 7],
    'Physics': [9, 8, 7, 6, 6, 8, 9, 6, 8, 9],
    'Russian': [8, 7, 8, 9, 6, 7, 8, 9, 8, 8],
    'English': [9, 8, 10, 9, 8, 9, 10, 9, 7, 8],
    'Biology': [7, 8, 9, 6, 7, 8, 9, 9, 8, 9]
}

df = pd.DataFrame(data)
print(df.head())

print('Mathematics', df['Mathematics'].mean())
print('Physics', df['Physics'].mean())
print('Russian', df['Russian'].mean())
print('English', df['English'].mean())
print('Biology', df['Biology'].mean())

print('Mathematics', df['Mathematics'].median())
print('Physics', df['Physics'].median())
print('Russian', df['Russian'].median())
print('English', df['English'].median())
print('Biology', df['Biology'].median())

print('Mathematics', df['Mathematics'].std())
print('Physics', df['Physics'].std())
print('Russian', df['Russian'].std())
print('English', df['English'].std())
print('Biology', df['Biology'].std())

Q1_math = df['Mathematics'].quantile(0.25)
Q3_math = df['Mathematics'].quantile(0.75)

IQR = Q3_math - Q1_math
print(IQR)