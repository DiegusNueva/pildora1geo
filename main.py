from geopy.geocoders import Nominatim
import time
import math

## Crear un objeto Nominatim
geo = Nominatim(user_agent="MyApp")

lugar = input("Dime un lugar: ")
loc = geo.geocode(lugar)
print(loc)
print(loc.latitude, loc.longitude)





