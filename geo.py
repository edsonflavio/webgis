from math import radians, cos, sin, asin, sqrt
# Implement the formula below
def distance_d(LaA, LaB, LoA, LoB):
    '''The function "radians" is found in the math module, It's also used to convert radians to degrees. 
        The Haversine formula for distance calculation
    '''
 
    LoA = radians(LoA)  
    LoB = radians(LoB)  
    LaA= radians(LaA)  
    LaB = radians(LaB) 
    # The "Haversine formula" is used.
    D_Lo = LoB - LoA 
    D_La = LaB - LaA 
    P = sin(D_La / 2)**2 + cos(LaA) * cos(LaB) * sin(D_Lo / 2)**2  
    
    Q = 2 * asin(sqrt(P))   
        # The earth's radius in kilometers.
    R_km = 6371  
    # Then we'll compute the outcome.
    return(Q * R_km)
# Import the geodesic module from geopy library 
from geopy.distance import geodesic as GD

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

def distance_g(LaA: float, LaB: float, LoA: float, LoB: float):
    '''Calculates the distance between two points in the earth usgin the latlong coordinates
    '''
    distance_geo = GD((LaA, LaB), (LoA, LoB))

    return distance_geo

LaA = 9.072264
LaB = 14.716677
LoA = 7.491302
LoB = -17.467686
print ("The distance between Abuja and Dakar is: ", distance_d(LaA, LaB, LoA, LoB), "K.M")  


# For the specified locations, load their latitude and longitude data.
Abuja ={"lat": 9.072264 , "long": 7.491302}
Dakar ={"lat": 14.716677 , "long": -17.467686}
#Finally, print the distance between the two sites in kilometers.
print("The distance between Abuja and Dakar is: ", distance_g(float(Abuja["lat"]), float(Abuja["long"]), float(Dakar["lat"]), float(Dakar["long"])).km)

# First, import the geopy library's great circle module.
from geopy.distance import great_circle as GRC
# Abuja and Dakar latitude and longitude data.
Abuja=(9.072264 , 7.491302)
Dakar=(14.716677 , -17.467686)
# Finally print the distance between the two points in km
print("The distance between Abuja and Dakar is:", GRC(Abuja,Dakar).km) 