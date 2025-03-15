import pandas as pd
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar

def hours_of_daylight(date, axis=23.44, latitude=47.61):
    """Compute the hours of daylight for the given date"""
    days = (date - pd.to_datetime('2000-12-21')).days
    m = (1. - np.tan(np.radians(latitude))
         * np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
    return 24. * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.



def prepare_data():
    counts = pd.read_csv('data/FremontBridge.csv', index_col='Date', parse_dates=True)
    weather = pd.read_csv('data/BicycleWeather.csv', index_col='DATE', parse_dates=True)

    daily = counts.resample('d').sum()
    daily['Total'] = daily.sum(axis=1)
    daily = daily[['Total']] 

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(7):
        daily[days[i]] = (daily.index.dayofweek == i).astype(float)


    cal = USFederalHolidayCalendar()
    holidays = cal.holidays('2012', '2016')
    daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
    daily['holiday'].fillna(0, inplace=True)

    daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))

    weather['TMIN'] /= 10
    weather['TMAX'] /= 10
    weather['Temp (C)'] = 0.5 * (weather['TMIN'] + weather['TMAX'])

    weather['PRCP'] /= 254
    weather['dry day'] = (weather['PRCP'] == 0).astype(int)


    daily = daily.join(weather[['PRCP', 'Temp (C)', 'dry day']])

    daily['annual'] = (daily.index - daily.index[0]).days / 365.




    daily.dropna(axis=0, how='any', inplace=True)
    return counts, weather, daily
