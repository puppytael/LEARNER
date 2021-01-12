# listing station names plus years
station = ["lighthouse"": ""2003", "Harmaja"":" "1989", "suomenlinna aaltopoiju" ":""2016", "kumpula"":""2005",
           "Kaisaniemi" ":""1844"]
print(station)
# listing stations
station_names = ["lighthouse", "Harmaja", "suomenlinna aaltopoiju", "kumpula", " Kaisaniemi"]
print(station_names)
# checking number of stations
assert station_names[0] == "lighthouse"
assert len(station_names) == 5, 'the station_names list should have 5 items'
#  listing station formation years
station_yr = [2003, 1989, 2016, 2005, 1844]
print(station_yr)
# Adding stations to station names plus years
station.append("Alajärvi Möksy"":""1957")
station.append("Alavus Sulkavankylä"":""1942")
print(station)
# can only add a single station using append
station_names.append("Alajärvi Möksy")
station_names.append("Alavus Sulkavankyl")
print(station_names)
# can add multiple stations using extend
station.extend(["Alajärvi Möksy"":""1957", "Alavus Sulkavankylä"":""1942"])
print(station)
station_names.extend(["Alajärvi Möksy", "Alavus Sulkavankylä"])
assert station_names[0] == 'lighthouse'
print(station_names)
station_yr.extend([2002, 2003])
print(station_yr)
assert len(station_yr) == 7, "the station start_yr should be 7"
# sort station in ascending order
station.sort()
print(station)
station_yr.sort()
print(station_yr)
station_yr.reverse()
print(station_yr)
station_names.sort()
print(station_names)
station_names.reverse()
print(station_names)
# combining two lists
x = zip(station_names, station_yr)
station_yr.sort(reverse=True)
print(tuple(x))
# showing temperature using list
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
average_temp = [-3.5, -4.5, -1, 4, 10, 15, 18, 16, 11.5, 6, 2, -1.5]
print(months)
print(average_temp)
assert len(months) == 12
"""
The following code works on the basis of index value.\nCorresponding elements of two lists are extracted using a common index value."""
selected_month_index = 6  # [0= Jan, ..., 11 = Dec, i.e. 4 = May]
selected_temp_index = selected_month_index
print_statement = "The average temperature in Helsinki in " + str(months[selected_month_index]) + " is " + str(
    average_temp[selected_temp_index])
print(print_statement)
assert len(months) == 12, 'correct length!'
assert len(average_temp) == 12, 'correct length!'
assert isinstance(months, list), 'Variable months is  a list'
assert isinstance(average_temp, list), 'Variable average_temp is  a list'
assert print_statement == "The average temperature in Helsinki in July is 18"
print()