#commit
# Assignment 6: Using Python to Explore Residential Water Use
# Created by: Joseph Brewer
# For: CEE6110 - Hydroinformatics: Horsburgh
#
# Description: This script accomplishes 2 things:
#   1. Comparisons between weekday and weekend water
#      consumption for Richards's Hall on USU's campus.
#   2. Describes the impact of sampling period on the estimate of
#      total water used over a time period.
#__________________________________________________________________


# Pseudocode

# 1.  import packages
# Pandas for dataframes and analytics
# Matplotlib for plotting functions

import pandas as pd
import matplotlib.pyplot as plt


# 2. read csv from Richards Hall and load data into pandas MAIN data frame
main_df = pd.read_csv('datalog_Richards_Hall.csv', header =1, sep = ',',index_col=0,
                 parse_dates=True, infer_datetime_format=True, low_memory=False)



# 3. Resample into hourly data

hourlyTotVol = main_df['IncrementalVolume'].resample(rule='1H', base = 0).sum()

# 4. Use index.dayofweek to split main data frame into weekday and weekend

week_hourlyTotVol = hourlyTotVol[hourlyTotVol.index.dayofweek <= 4]
weekend_hourlyTotVol = hourlyTotVol[hourlyTotVol.index.dayofweek >=5]


# 5. Aggregate into average hourly volume for weekday and weekend
# with groupby function

# Week stats
week_hourlyAvgVol = week_hourlyTotVol.groupby(week_hourlyTotVol.index.hour).mean()
week_hourlyStdVol = week_hourlyTotVol.groupby(week_hourlyTotVol.index.hour).std()

# Weekend stats
weekend_hourlyAvgVol = weekend_hourlyTotVol.groupby(weekend_hourlyTotVol.index.hour).mean()
weekend_hourlyStdVol = weekend_hourlyTotVol.groupby(weekend_hourlyTotVol.index.hour).mean()



# 6. Plot average hourly weekday water demand vs average hourly weekend water demand

fig, ax = plt.subplots()

plt.errorbar(x=week_hourlyAvgVol.index, y=week_hourlyAvgVol,
             yerr=week_hourlyStdVol, capsize=3,
             capthick=0.5, fmt='--',
             label='Weekday', marker='o')



plt.errorbar(x = weekend_hourlyAvgVol.index, y = weekend_hourlyAvgVol,
             yerr=weekend_hourlyStdVol, capsize=3,
             capthick=0.5, fmt='--',
             label = 'Weekend', marker='o')

ax.legend(loc='upper left')
ax.set_title('Average Hourly Volumes - Richards Hall')
ax.set_ylabel('Flow (gph)')
ax.set_xlabel('Hours (Midnight - Midnight)')




# 7. Slice 2017-03-03 15:13:00 and 2017-03-27 16:20 from MAIN data frame

# 8. resample date slice

# 9. Determine sum of various resampling sizes.
plt.show()

print('done')