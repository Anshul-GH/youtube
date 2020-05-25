# select * from table where
# column_name = some_value

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
                   'B': 'one one two three two two one three'.split(),
                   'C': np.arange(8), 'D': np.arange(8) * 2})

# print(df)

# print(df.loc[df['A'] == 'foo'])

# print(df.loc[df['B'].isin(['one', 'three'])])

df = df.set_index(['B'])
# print(df.loc['one'])
print(df.loc[df.index.isin(['one', 'three'])])