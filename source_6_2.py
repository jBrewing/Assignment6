

# 1. import packages
import pandas as pd
import matplotlib.pyplot as plt

# 2. read csv from Richards Hall and load data into pandas MAIN data frame
df_main = pd.read_csv('datalog_Richards_Hall.csv', header =1, sep = ',',index_col=0,
                 parse_dates=True, infer_datetime_format=True, low_memory=False)

df_manual = pd.read_csv('manual_meter_readings_richards_hall.csv', header=1, sep=',', index_col=0,
                        parse_dates=True, infer_datetime_format=True)

# 4. Slice 2017-03-03 15:13:00 and 2017-03-27 16:20 from MAIN data frame

beginDate = '2017-03-03 15:13:00'
endDate = '2017-03-27 16:20:00'

df_resample = df_main[beginDate:endDate].copy()

# 5. Subsample full 1s resolution into 30s, 1m, 1h, 24h.

df_5s = df.resample[0::5].copy()
df_10s = df_resample[0::10].copy()
df_30s = df_resample[0::30].copy()
