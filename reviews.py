import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv.zip", compression="zip")

grouped_data = df.groupby("country")["points"].agg(
    count=pd.Series.count,  
    points=pd.Series.mean  
).reset_index()

grouped_data = grouped_data.sort_values(by="count", ascending=False)

grouped_data["points"] = grouped_data["points"].round(1)
grouped_data[["country", "count", "points"]].to_csv("reviews-per-country.csv", index=False)

