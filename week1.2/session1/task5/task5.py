# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["manchester"] = "nile"
rivers["york"] = "idk"
print(rivers)
# Display all the keys
cities = rivers.keys()
print(cities)
# Display all the values
water = rivers.values()
print(water)
# Display all the key:value pairs, as tuples
everything = rivers.items()
print(everything)
# Delete an entry from the rivers database
rivers.pop("york")
print(rivers)
