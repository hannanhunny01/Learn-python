#You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
print(travel_log[0])
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
#def travel_log(country,visit,)
def add_new_country(countryname,visits,cities):
    dict ={"country":countryname,"cities":visits,"cities":cities}
    travel_log.append(dict)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
