import pandas as pd
import datetime as dt

pre_pivot = pd.read_csv('/Volumes/Trim_SSD/Oman/Oman-Bisat_Field/DP_Timebased/BST_7_Drilling_Parameters_A.csv')
print('loaded successfully')
pre_pivot['Date Time'] = pd.to_datetime(pre_pivot['Date Time'])
print('date converted')
pre_pivot['Epoch'] = (pre_pivot['Date Time'] - dt.datetime(1970,1,1)).dt.total_seconds()
print('done with epoch')
pre_pivoted = pre_pivot.drop(columns = "Date Time")
print(pre_pivoted)
post_pivot= pd.melt(pre_pivoted, id_vars='Epoch', var_name='tag_name', value_name='Value')


print(post_pivot.head(15))

post_pivot.to_csv(r'/Volumes/Trim_SSD/Oman/Oman-Bisat_Field/DP_Timebased/test.csv', index =None, header=True)

print("done")
