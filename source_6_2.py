

# 1. import packages
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table

# 2. read csv from Richards Hall and load data into pandas MAIN data frame
df_main = pd.read_csv('datalog_Richards_Hall.csv', header =1, sep=',',index_col=0,
                 parse_dates=True, infer_datetime_format=True, low_memory=False)

df_manual = pd.read_csv('manual_meter_readings_richards_hall.csv', header=0, sep=',', index_col=0,
                        parse_dates=True, infer_datetime_format=True)

# 4. Slice 2017-03-03 15:13:00 and 2017-03-27 16:20 from MAIN data frame

beginDate = '2017-03-03 15:13:00'
endDate = '2017-03-27 16:20:00'


df_resample = df_main[beginDate:endDate].copy()
df_manual = df_manual[beginDate:endDate].copy()

# 5. Subsample full 1s resolution into 30s, 1m, 1h, 24h.

df_1s = df_resample
df_5s = df_resample[0::5].copy()
df_10s = df_resample[0::10].copy()
df_30s = df_resample[0::30].copy()

df_5s['TotVol'] = df_5s['IncrementalVolume'].cumsum()
df_10s['TotVol'] = df_10s['IncrementalVolume'].cumsum()
df_30s['TotVol'] = df_30s['IncrementalVolume'].cumsum()

last =[['108484 gal', '21696 gal', '10849 gal', '3604 gal', '110248 gal']]
df_summary = pd.DataFrame(last, columns=('1s total', '5s total', '10s total', '30s total', 'manual total'))

# 6. plot stuff

# plot incremental volume
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,6))

ax1.plot(df_1s['TotalizedVolume'], label='1s')
ax1.plot(df_5s['TotVol'], label='5s')
ax1.plot(df_10s['TotVol'], label='10s')
ax1.plot(df_30s['TotVol'], label='30s')
ax1.plot(df_manual['Volume_Used_gal'], marker='o', label='Manual readings')
ax1.set_title('Cumulative Volume with Decimated Data Resolution: 1s, 5, 10s, 30s, & Manual\n '
              'Total Cumulative Volume displayed below')
ax1.set_xlabel('Date (MST)')
ax1.set_ylabel('Cumulative Volume (gal)')


ax2.table(cellText =df_summary.values, colLabels=df_summary.columns, loc='upper center')
ax2.axis('tight')
ax2.axis('off')
ax2.set_ylabel('Total Cumulative Volume')





#df_1s.plot(y='TotalizedVolume', ax=ax, kind='line', use_index=True,
#            label = '1s Data')
#df_5s.plot(y='TotVol', ax=ax, kind='line', use_index=True,
#            label = '5s Data')
#df_10s.plot(y='TotVol', ax=ax, kind='line', use_index=True,
#            label = '10s Data')
#df_30s.plot(y='TotVol', ax=ax, kind='line', use_index=True,
#            label = '30s Data')
#df_manual.plot(y='Volume_Used_gal', ax=ax, kind='line', use_index=True,
#                marker = 'o', label = 'Manual Meter')
#ax.set_title('Cumulative Volume with Decimated Data Resolution: 1s, 5, 10s, 30s, & Manual')
#ax.set_xlabel('Date (MST)')
#ax.set_ylabel('Cumulative Volume (gal)')

plt.show()


print('done')
