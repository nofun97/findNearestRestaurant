from functions import find_closest_restaurant_in_neighbourhood as fcrn, \
                            find_restaurant_coordinates
from math import sqrt

def find_closest_restaurant(x, y):
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


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_closest_restaurant(1.0, 1.0))
    print(find_closest_restaurant_on_path([[1.0, 1.0], [4.5, 4.0]]))
