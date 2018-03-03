from math import sqrt
def find_restaurant_coordinates(restaurant):
    '''
    function find_restaurant_coordinates takes a name of a restaurant
    and returns the exact coordinate
    '''
    # if a restaurant ends in 'CR' the coordinate is an integer
    if 'CR' in restaurant:
        y_axis = ord(restaurant[0]) - 65
        x_axis = int(restaurant.strip('ABCDEFGHIJMR')) - 1
    # if a restaurant ends in 'MR' the coordinate is a float ending with '.5'
    else:
        y_axis = ord(restaurant[0]) - 65 + 0.5
        x_axis = int(restaurant.strip('ABCDEFGHIJMR')) - 0.5
    return x_axis, y_axis

def find_my_neighbourhood(x, y):
    '''
    function find_my_neighbourhood takes two integers x and y
    and returns the name of the neighbourhood based on the
    coordinates
    '''
    letters = 'ABCDEFGHIJ'
    coordinates = []
    # creating the coordinates into a list of lists
    for letter in letters:
        y_axis = []
        for number in range(1, 11):
            y_axis.append(letter + str(number))
        # adding the coordinates to a list
        coordinates.append(y_axis)
    return coordinates[int(y)][int(x)]

def find_all_restaurants_in_neighbourhood(x, y):
    '''
    function find_all_restaurants_in_neighbourhood takes two integers
    x and y and returns the name of restaurants in the neighbourhood
    '''
    # using the function find_my_neighbourhood to get the name 
    # of the neighbourhood
    coordinate = find_my_neighbourhood(x, y)
    return list((coordinate + 'CR', coordinate + 'MR'))

def find_closest_restaurant_in_neighbourhood(x, y):
    '''
    function find_closest_restaurant_in_neighbourhood takes two integers
    x and y as coordinate and returns the closest restaurants from the 
    coordinate in one neighbourhood
    '''
    # getting all the restaurants in one neighbourhood
    restaurants = find_all_restaurants_in_neighbourhood(x, y)
    result = []
    dist = []
    
    # putting the distances of the restaurants in a neighbourhood from the
    # point into a list of distances
    for restaurant in restaurants:
        x_rest, y_rest = find_restaurant_coordinates(restaurant)
        dist.append(sqrt((x-x_rest)**2 + (y-y_rest)**2))
        
    # if the first restaurant is closer, it is added to the list
    if dist[0] < dist[1]:
        result.append(restaurants[0])
    # if the second restaurant is closer, it is added to the list
    elif dist[1] < dist[0]:
        result.append(restaurants[1])
    # if both restaurants are the same distance from the point
    # both restaurants are returned
    else:
        return restaurants
    return result

def find_closest_restaurant(x, y,
                            fcrn=find_closest_restaurant_in_neighbourhood):
    '''
    function find_closest_restaurant takes two integers x and y and returns the
    closest restaurant from the point in multiple neighbourhoods
    '''
    
    closest_restaurants = []
    possible_restaurants = []
    # the shortest possible distance
    shortest_dist = sqrt(0.5**2 + 0.5**2)
    
    # adding the possible restaurants in the closest neighbourhood from (x,y)
    for restaurant in fcrn(x, y):
        possible_restaurants.append(restaurant)
        
    # taking other restaurants from other possible neighbouring places 
    for n in range(1, 3):
        for restaurant in fcrn(x+(0.5*(-1)**n), y+(0.5*(-1)**n)):
            possible_restaurants.append(restaurant)
        for restaurant in fcrn(x+(0.5*(-1)**n), y+(0.5*(-1)**(n+1))):
            possible_restaurants.append(restaurant)
    
    # removing duplicates
    possible_restaurants = list(set(possible_restaurants))
    
    # counting the distances of possible restaurants from the point x,y
    for restaurant in possible_restaurants:
        x_rest, y_rest = find_restaurant_coordinates(restaurant)
        dist = sqrt((x-x_rest)**2 + (y-y_rest)**2)
        # if the distance from a restaurant is less than the shortest
        # possible distance, then the restaurant is added to the result
        # it also clears the result and changes the shortest possible distance
        if dist < shortest_dist:
            closest_restaurants.clear()
            closest_restaurants.append(restaurant)
            shortest_dist = dist
        # if a restaurant's distance from the point is the same as the shortest
        # possible distance, then it is added to the result
        elif dist == shortest_dist:
            closest_restaurants.append(restaurant)
            
    # returns the sorted restaurant
    return sorted(closest_restaurants)

def find_closest_restaurant_on_path(list_of_stops):
    '''
    function find_closest_restaurant_on_path takes a list of points as
    list_of_stops and returns the closest restaurants from these points
    '''
    
    restaurants = []
    # using the find_closest_restaurant function to find closest restaurants
    # near the points
    for (x, y) in list_of_stops:
        restaurants.append(find_closest_restaurant(x, y))
    return restaurants
