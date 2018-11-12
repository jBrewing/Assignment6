#commit
# Assignment 6: Using Python to Explore Residential Water Use
# Created by: Joseph Brewer
# For: CEE6110 - Hydroinformatics: Horsburgh
#
# Description: These scripts will accomplish 2 things:
#   Script 1. Make comparisons between weekday and weekend water
#      consumption for Richards's Hall on USU's campus.
#            - average hourly volume consumed with std. dev bars
#            - boxplot for range, mean, and IQR
#            - histogram for frequency distribution
#   Script 2. Describe the impact of sampling period on the estimate of
#      total water used over a time period.
#__________________________________________________________________


# Pseudocode

# 1.  import packages
# Pandas for dataframes and analytics
# Matplotlib for plotting functions

import pandas as pd
import matplotlib.pyplot as plt



# 2. read csv from Richards Hall and load data into pandas MAIN data frame
# infer_datetime_format, parse_dates, and index_col combine to set date as index,
# thereby enabling queries based on dates.
df_main = pd.read_csv('datalog_Richards_Hall.csv', header =1, sep = ',',index_col=0,
                 parse_dates=True, infer_datetime_format=True, low_memory=False)



# 3. Resample into hourly data with dataframe.resample.
# .sum() sums incremental volume for each hourly resample.

hourlyTotVol = df_main['IncrementalVolume'].resample(rule='1H', base = 0).sum()


# 4. Use index.dayofweek to split main data frame into weekday and weekend

week_hourlyTotVol = hourlyTotVol[hourlyTotVol.index.dayofweek <= 4]
weekend_hourlyTotVol = hourlyTotVol[hourlyTotVol.index.dayofweek >=5]


# 5. Aggregate into average hourly volume for weekday and weekend
# with groupby function.  This averages the hourly consumption into a 24 hour frame for each day.
# i.e. the average hourly consumption for ALL weekdays and the average hourly consumption for ALL
# weekend days.

# Week stats
# Mean and std.dev
week_hourlyAvgVol = week_hourlyTotVol.groupby(week_hourlyTotVol.index.hour).mean()
week_hourlyStdVol = week_hourlyTotVol.groupby(week_hourlyTotVol.index.hour).std()


# Weekend stats
# Mean and std.dev
weekend_hourlyAvgVol = weekend_hourlyTotVol.groupby(weekend_hourlyTotVol.index.hour).mean()
weekend_hourlyStdVol = weekend_hourlyTotVol.groupby(weekend_hourlyTotVol.index.hour).mean()


# 6. Plot average hourly weekday water demand vs average hourly weekend water demand
# Plot as line with standard deviation bars.

gridsize =(3,2)
fig = plt.figure(figsize=(12,8))
ax1 = plt.subplot2grid(gridsize, (0,0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2,0))
ax3 = plt.subplot2grid(gridsize, (2,1))
axis_font = {'fontname':'Arial', 'size':'9'}
ax1.errorbar(x=week_hourlyAvgVol.index + 0.08, y=week_hourlyAvgVol,
             yerr=week_hourlyStdVol, capsize=3,
             capthick=0.5, fmt='--',
             label='Weekday (Mon-Fri)', marker='o')

ax1.errorbar(x = weekend_hourlyAvgVol.index, y = weekend_hourlyAvgVol,
             yerr=weekend_hourlyStdVol, capsize=3,
             capthick=0.5, fmt='--',
             label = 'Weekend (Sat-Sun)', marker='o')

ax1.legend(loc='upper left')
ax1.set_title('Average Hourly Volumes - Richards Hall with error bars.  Hours(x-axis) vs Total Gallons Used(y-axis)',
              fontsize=14)

# Plot as boxplot to see range, mean, and IQR.

# Convert data to list.  More efficient to plot as two boxplots in same
# Axes since boxplot converts a 2-D array into list of vectors anyway.
data = [week_hourlyAvgVol, weekend_hourlyAvgVol]
ax2.boxplot(x=data, notch=True, showmeans=True)
ax2.set_title('Consumption Range', fontsize=8)
ax2.set_xlabel('Week (1), Weekend (2)')
ax2.set_ylabel('Gallons Consumed')

# Plot as histogram to see frequency of consumption in hourly time frame.
data2 = [week_hourlyTotVol, weekend_hourlyTotVol]
ax3.hist(data, label=('Week (Mon-Fri)', 'Weekend (Sat-Sun)'))
ax3.legend(loc='upper left')
ax3.set_title('Freq. of Consumption Intervals', fontsize = 8)
ax3.set_ylabel('Frequency')
ax3.set_xlabel('Gallons Consumed')

date1 = '2017-03-07 13:39:00'
date2 = '2017-03-17 13:20:00'
date3 = '2017-03-20 09:51:00'
date4 = ''

plt.show()

print('done')