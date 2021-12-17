# # # # select * from table where
# # # # column_name = some_value

# # # import pandas as pd
# # # import numpy as np

# # # df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
# # #                    'B': 'one one two three two two one three'.split(),
# # #                    'C': np.arange(8), 'D': np.arange(8) * 2})

# # # # print(df)

# # # # print(df.loc[df['A'] == 'foo'])

# # # # print(df.loc[df['B'].isin(['one', 'three'])])

# # # df = df.set_index(['B'])
# # # # print(df.loc['one'])
# # # print(df.loc[df.index.isin(['one', 'three'])])




# # # Learn Pandas - how to iterate over rows in a dataframe in pandas


# # import pandas as pd
# # inp = [{'c1':10, 'c2':20}, {'c1': 11, 'c2': 21}, {'c1': 12, 'c2': 22}]

# # df = pd.DataFrame(inp)

# # # print(df)

# # for index, row in df.iterrows():
# #     print(row['c1'], row['c2'])

# '''
# year	key	val
# 2019	a  	3
# 2019	a  	4
# 2019	b  	3
# 2019	c  	5
# 2020	d  	6
# 2020	e  	1
# 2020	f  	2
# '''

# # import pandas as pd

# # df = pd.read_clipboard()

# # # print(df)

# # # df.insert(1, 'prev_year', df['year'] - 1)

# # df['prev_year'] = df['year'] - 1

# # print(df)

# '''
# brand        model      year       engine    transmission   suspension   brakes   Overall_Score
# Acura        CL         1999          3           2           1           3          1
# Acura        CL         2000          5           3           7           2          3
# BMW          520        2015          22          4           10          11         2
# BMW          520        2008          1           6           3           6          4
# Chevrolet    Impala     1997          0           2           2           5          1
# Chevrolet    Impala     2002          9           3           8           4          1
# '''

# import pandas as pd

# df = pd.read_clipboard()

# cols = df.select_dtypes(include='int').columns

# df[cols] = df[cols].astype(float)

# print(df)

'''
col1    col2    col3    col4    col5
False   False   True    True    False
False   True    True    False   False
'''





























