import pandas as pd

pd.options.display.max_columns = 999
videos = pd.read_excel('./Videos.xlsx', index_col='Month')
print(videos.T)