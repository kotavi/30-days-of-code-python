import pandas as pd

olympic_df = pd.read_csv("olympics/olympic.csv", skiprows=4)

# print(olympic_df.head())
print(olympic_df.shape)
print(olympic_df.info())
print(olympic_df[["City", "Event"]])
print(type(olympic_df[["City", "Event"]]))
print(type(olympic_df["City"]))

print("-*-" * 50)

unique_cities_count = olympic_df["Edition"].value_counts()
print(unique_cities_count)
gender_count = olympic_df["Gender"].value_counts()
print(gender_count)

sorted_athletes = olympic_df.Athlete.sort_values()
print(sorted_athletes)

print(olympic_df.sort_values(by=["Edition", "Athlete"]))

print(olympic_df.Medal == "Gold")
print(olympic_df[(olympic_df.Medal == "Gold") & (olympic_df.Gender == "Women")])



