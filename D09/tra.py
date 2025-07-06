travle_log=[
   {
        "countries":"Ethiopia",
        "visits":4,
        "cities":["DT","BDR","Injibara","Addis Ababa"]
    },
]

country=input("Enter The Country you have already visited?:")
visits=int(input("How Many Times you viit it?:"))
cities = input("Enter Items Separated by space?:")
cities = cities.split()

def add_travel_counties(country,visits,cities):
    travle_log.append({"countries": country,"visits":visits,"cities":cities})

add_travel_counties(country=country,visits=visits,cities=cities)
length_of_travel=len(travle_log)

# print(length_of_travel-1)
# print(travle_log[length_of_travel-1]["countries"])

print(f"I've been {travle_log[length_of_travel-1]["countries"]} {travle_log[length_of_travel-1]["visits"]} time's")
print(f"My favorite city {travle_log[length_of_travel-1]["cities"][0]}")