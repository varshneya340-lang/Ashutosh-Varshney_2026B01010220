# AIRSCOPE - AQI DATA ANALYSIS PROJECT

import csv

print("Welcome to AirScope!")
print("My First Data Analysis Project")



city = "Delhi"
temperature = 28.5
humidity = 65
aqi = 185

print("\n===== CITY INFORMATION =====")
print("City:", city)
print("Temperature:", temperature, "C")
print("Humidity:", humidity, "%")
print("AQI:", aqi)

print("\n===== DATA TYPES =====")
print(type(city))
print(type(temperature))
print(type(humidity))
print(type(aqi))





cities = ["Delhi", "Noida", "Ghaziabad", "Lucknow"]

print("\n===== CITIES IN OUR PROJECT =====")

for city in cities:
    print(city)

print("Total cities:", len(cities))


aqi_data = {
    "city": "Delhi",
    "temperature": 28.5,
    "humidity": 65,
    "aqi": 185
}



print("\n===== AQI DICTIONARY =====")

print("City:", aqi_data["city"])
print("Temperature:", aqi_data["temperature"])
print("Humidity:", aqi_data["humidity"])
print("AQI:", aqi_data["aqi"])

# Displaying all dictionary data

print("\nComplete AQI Data:")
print(aqi_data)
# hastag creates a comment in python 
# { creates dictionaries in python 
# string value is for texts 
# print (" any thing inside this ") simply prints the texts as it is 
# len is used for no of things to itself 
# for loop single continued action for more datasets 
# list is like if i  have to name the four cities thrn instead of applying 4 times the data type to it we just add in single bracket by comma 
# for is to tell repeating occurs  then 'city' is variable name which storing the data  of cities and cities is list 'print(city)' is to print purpose 
print("\n----- AQI ANALYSIS -----")

if aqi <= 50:
    print("Air Quality: Good")

elif aqi <= 100:
    print("Air Quality: Satisfactory")

elif aqi <= 200:
    print("Air Quality: Moderate")

elif aqi <= 300:
    print("Air Quality: Poor")

elif aqi <= 400:
    print("Air Quality: Very Poor")

elif aqi <= 500:
    print("Air Quality: Severe")

else:
    print("Invalid AQI value")
    import csv

print("\n----- READING CSV DATA -----")
with open("aqi_data.csv", "r") as file:
    reader = csv.DictReader(file)
    all_records = [row for row in reader if row["AQI"].strip().isdigit()]

print("\n===== DATASET VERIFICATION =====")
total_records = len(all_records)
print("Total AQI Records:", total_records)

for row in all_records:
    print(row)

print("\n===== AIRSCOPE DATA ANALYSIS =====")
aqi_values = [int(row["AQI"].strip()) for row in all_records]


            
total_records = len(aqi_values)
average_aqi = sum(aqi_values) / total_records if total_records > 0 else 0
highest_aqi = max(aqi_values) if aqi_values else 0
print("Total Records:", total_records)
print("Average AQI:", round(average_aqi, 2))
print("Highest AQI:", highest_aqi)