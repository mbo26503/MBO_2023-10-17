# 20/10/2023 15:08
# excel
import pandas as pd
import numpy as np
import openpyxl
# pip install pandas
technologies = ['Spark', 'Pandas', 'Java', 'Python', 'PHP']
fee = [25000, 2000, 15000, 15000, 18000]
duration = ['50 Days', '35 Days', np.nan, '30 Days', '30 Days']
discount = [2000, 1000, 500, 800, 500]
columns = ['courses', 'Fee', 'Duration', 'Discount']

df = pd.DataFrame(list(zip(technologies, fee, duration, discount)), columns=columns)

print(df)
df.to_excel('Courses.xlsx', index=False)