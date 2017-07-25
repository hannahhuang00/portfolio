import pandas
import matplotlib.pyplot as plt
from datetime import datetime


data = pandas.read_csv("weather_year.csv")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

first_date = data.date.values[0]
datetime.strptime(first_date, "%Y-%m-%d")

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))

data.index = data.date

data = data.drop(["date"], axis=1)

empty = data.apply(lambda col: pandas.isnull(col))

#print(data.dropna(subset=["events"]))

data.events = data.events.fillna("")

num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1

freezing_days = data[data.max_temp <= 32]
freezing_days[freezing_days.min_temp >= 20]

temp_max = data.max_temp <= 32

temp_min = data.min_temp >= 20

temp_both = temp_min & temp_max

cover_temps = {}
for cover, cover_data in data.groupby("cloud_cover"):
    cover_temps[cover] = cover_data.mean_temp.mean()

for (cover, events), group_data in data.groupby(["cloud_cover", "events"]):
    print "Cover: {0}, Events: {1}, Count: {2}".format(cover, events, len(group_data))
